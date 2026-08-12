"""Shared dump tree — framework-agnostic value inspection."""

from __future__ import annotations

import ast
import inspect
import linecache
import os
from dataclasses import dataclass, field
from pathlib import Path
from types import FrameType
from typing import Any

_PROJECT_ROOT: Path | None = None
_PACKAGE = Path(__file__).resolve().parent
DEFAULT_MAX_DEPTH = 4


def set_project_root(path: Path | str | None) -> None:
    global _PROJECT_ROOT
    _PROJECT_ROOT = Path(path).resolve() if path else None


def project_root() -> Path:
    return _PROJECT_ROOT or Path.cwd()


def _first_user_frame(*, skip_packages: tuple[str, ...] = ()) -> FrameType | None:
    root = project_root()
    skip = (_PACKAGE, *(Path(p).resolve() for p in skip_packages if Path(p).exists()))
    for frame_info in inspect.stack()[1:]:
        raw = frame_info.filename
        if raw.startswith('<'):
            continue
        path = Path(raw).resolve()
        if any(path.is_relative_to(s) for s in skip):
            continue
        return frame_info.frame
    return None


def _frame_location(frame: FrameType) -> str | None:
    root = project_root()
    raw = frame.f_code.co_filename
    if raw.startswith('<'):
        return None
    path = Path(raw).resolve()
    try:
        shown = path.relative_to(root).as_posix()
    except ValueError:
        shown = os.path.basename(raw)
    return f'{shown}:{frame.f_lineno}'


def caller_frame(*, skip_packages: tuple[str, ...] = ()) -> str | None:
    """First user frame as path:line. skip_packages extra roots to ignore."""
    frame = _first_user_frame(skip_packages=skip_packages)
    return _frame_location(frame) if frame is not None else None


def _expr_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _expr_name(node.value)
        return f'{base}.{node.attr}' if base else node.attr
    if isinstance(node, ast.Subscript):
        base = _expr_name(node.value)
        return f'{base}[…]' if base else None
    if isinstance(node, ast.Call):
        base = _expr_name(node.func)
        return f'{base}(…)' if base else None
    if isinstance(node, ast.Constant):
        return repr(node.value)
    return None


def _call_arg_names(line: str) -> list[str | None]:
    stripped = line.strip()
    if not stripped:
        return []
    try:
        tree = ast.parse(stripped)
    except SyntaxError:
        return []

    call: ast.Call | None = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            call = node
    if call is None:
        return []

    return [_expr_name(arg) for arg in call.args]


def caller_arg_names(*, skip_packages: tuple[str, ...] = ()) -> list[str | None]:
    """Variable names passed positionally to the dump call on the user frame."""
    frame = _first_user_frame(skip_packages=skip_packages)
    if frame is None:
        return []
    line = linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()
    if not line:
        return []
    return _call_arg_names(line)


def value_kind(value: Any) -> str:
    if isinstance(value, (bool, int, float, str)) or value is None:
        return 'scalar'
    if isinstance(value, dict):
        return 'dict'
    if isinstance(value, list):
        return 'list'
    if isinstance(value, tuple):
        return 'tuple'
    if isinstance(value, set):
        return 'set'
    if isinstance(value, type):
        return 'class'
    if inspect.ismethod(value):
        return 'method'
    if inspect.isfunction(value) or inspect.isbuiltin(value):
        return 'function'
    if inspect.isroutine(value):
        return 'callable'
    return 'object'


def value_type_name(value: Any) -> str:
    if isinstance(value, type):
        return value.__qualname__
    return type(value).__qualname__


def describe_value(value: Any, *, name: str | None = None) -> str:
    """Human summary: ``$connection · object · CursorResult``."""
    parts: list[str] = []
    if name:
        parts.append(f'${name}')
    parts.append(value_kind(value))
    parts.append(value_type_name(value))
    return ' · '.join(parts)


def format_dump_tip(
    value: Any,
    *,
    source: str | None = None,
    name: str | None = None,
    skip_packages: tuple[str, ...] = (),
) -> str:
    if source is None:
        source = caller_frame(skip_packages=skip_packages)
    meta = describe_value(value, name=name)
    if source and meta:
        return f'{source} · {meta}'
    return source or meta


@dataclass
class DumpNode:
    """One printable dump fragment."""

    kind: str  # scalar | container | object | recursion | truncated
    label: str = ''
    text: str = ''
    scalar_kind: str = ''  # None|bool|int|float|str|other
    children: list[tuple[str, DumpNode]] = field(default_factory=list)


def _note(value: Any) -> str:
    if isinstance(value, dict):
        return f'dict:{len(value)}'
    if isinstance(value, list):
        return f'list:{len(value)}'
    if isinstance(value, tuple):
        return f'tuple:{len(value)}'
    if isinstance(value, set):
        return f'set:{len(value)}'
    return type(value).__name__


def _truncated_node(value: Any) -> DumpNode:
    return DumpNode(kind='truncated', text=f'<max depth {type(value).__name__}>')


def _scalar_node(value: Any) -> DumpNode:
    if value is None:
        return DumpNode(kind='scalar', text='None', scalar_kind='None')
    if isinstance(value, bool):
        return DumpNode(kind='scalar', text='True' if value else 'False', scalar_kind='bool')
    if isinstance(value, int):
        return DumpNode(kind='scalar', text=str(value), scalar_kind='int')
    if isinstance(value, float):
        return DumpNode(kind='scalar', text=repr(value), scalar_kind='float')
    if isinstance(value, str):
        shown = value if len(value) <= 160 else value[:160] + '…'
        return DumpNode(kind='scalar', text=shown, scalar_kind='str')
    return DumpNode(kind='scalar', text=repr(value), scalar_kind='other')


def _public_attrs(mapping: dict[str, Any]) -> dict[str, Any]:
    return {
        k: v for k, v in mapping.items()
        if not k.startswith('_') and not callable(v)
    }


def _callable_node(value: Any) -> DumpNode:
    if inspect.ismethod(value):
        label = 'method'
    elif inspect.isfunction(value):
        label = 'function'
    elif inspect.isbuiltin(value):
        label = 'builtin'
    else:
        label = type(value).__name__

    children: list[tuple[str, DumpNode]] = []
    name = getattr(value, '__name__', None)
    if name is not None:
        children.append(('attr:name', _scalar_node(name)))
    module = getattr(value, '__module__', None)
    if module:
        children.append(('attr:module', _scalar_node(module)))
    try:
        children.append(('attr:signature', _scalar_node(str(inspect.signature(value)))))
    except (TypeError, ValueError):
        pass
    try:
        src = inspect.getsourcefile(value)
        if src:
            lines = inspect.getsourcelines(value)
            children.append(('attr:file', _scalar_node(f'{src}:{lines[1]}')))
    except (TypeError, OSError):
        pass

    if not children:
        return _scalar_node(value)
    return DumpNode(kind='object', label=label, children=children)


def _class_node(
    value: type,
    *,
    depth: int,
    max_depth: int,
    seen: set[int],
) -> DumpNode:
    children: list[tuple[str, DumpNode]] = []
    module = getattr(value, '__module__', None)
    if module:
        children.append(('attr:module', _scalar_node(module)))
    bases = tuple(b.__name__ for b in value.__bases__ if b is not object)
    if bases:
        children.append((
            'attr:bases',
            inspect_value(bases, depth=depth + 1, max_depth=max_depth, seen=seen),
        ))
    attrs = _public_attrs(dict(vars(value)))
    for k, v in attrs.items():
        children.append((
            f'attr:{k}',
            inspect_value(v, depth=depth + 1, max_depth=max_depth, seen=seen),
        ))
    if not children:
        return DumpNode(kind='object', label=f'{value.__name__} (class)', children=[
            ('attr:module', _scalar_node(module or '')),
        ])
    return DumpNode(kind='object', label=f'{value.__name__} (class)', children=children)


def _instance_node(
    value: Any,
    *,
    depth: int,
    max_depth: int,
    seen: set[int],
) -> DumpNode | None:
    attrs: dict[str, Any] = {}
    if hasattr(value, '__dict__'):
        attrs.update(_public_attrs(vars(value)))
    slots = getattr(type(value), '__slots__', ())
    if isinstance(slots, str):
        slots = (slots,)
    for name in slots:
        if name.startswith('_'):
            continue
        try:
            v = getattr(value, name)
        except AttributeError:
            continue
        if callable(v):
            continue
        attrs.setdefault(name, v)
    if not attrs:
        return None
    children = [
        (
            f'attr:{k}',
            inspect_value(v, depth=depth + 1, max_depth=max_depth, seen=seen),
        )
        for k, v in attrs.items()
    ]
    return DumpNode(
        kind='object',
        label=f'{type(value).__name__} ({value_kind(value)})',
        children=children,
    )


def inspect_value(
    value: Any,
    *,
    depth: int = 0,
    max_depth: int = DEFAULT_MAX_DEPTH,
    seen: set[int] | None = None,
) -> DumpNode:
    """Walk value → DumpNode tree (used by text + HTML formatters)."""
    if depth >= max_depth:
        return _truncated_node(value)

    if seen is None:
        seen = set()

    oid = id(value)
    is_container = isinstance(value, (dict, list, tuple, set)) or (
        (hasattr(value, '__dict__') or hasattr(type(value), '__slots__'))
        and not isinstance(value, type)
        and not (inspect.isroutine(value) or inspect.ismethod(value))
    )
    if is_container:
        if oid in seen:
            return DumpNode(kind='recursion', text=f'<recursion {type(value).__name__}>')
        seen = set(seen) | {oid}

    if isinstance(value, dict):
        children: list[tuple[str, DumpNode]] = []
        for k, v in value.items():
            key = f'str:{k}' if isinstance(k, str) else f'idx:{k}'
            children.append((
                key,
                inspect_value(v, depth=depth + 1, max_depth=max_depth, seen=seen),
            ))
        return DumpNode(kind='container', label=_note(value), children=children)

    if isinstance(value, (list, tuple, set)):
        children = [
            (
                f'idx:{i}',
                inspect_value(v, depth=depth + 1, max_depth=max_depth, seen=seen),
            )
            for i, v in enumerate(value)
        ]
        return DumpNode(kind='container', label=_note(value), children=children)

    if isinstance(value, type):
        return _class_node(value, depth=depth, max_depth=max_depth, seen=seen)

    if inspect.isroutine(value) or inspect.ismethod(value):
        return _callable_node(value)

    instance = _instance_node(value, depth=depth, max_depth=max_depth, seen=seen)
    if instance is not None:
        return instance

    return _scalar_node(value)
