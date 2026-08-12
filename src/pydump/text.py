"""ANSI / plain text formatter for DumpNode trees."""

from __future__ import annotations

import os
import sys

from pydump.core import (
    DumpNode,
    caller_arg_names,
    caller_frame,
    format_dump_tip,
    inspect_value,
)

# ANSI color palette (24-bit when TTY)
_C = {
    'reset': '\033[0m',
    'orange': '\033[38;2;255;132;0m',
    'blue': '\033[38;2;18;153;218m',
    'green': '\033[38;2;86;219;58m',
    'gray': '\033[38;2;160;160;160m',
    'white': '\033[38;2;255;255;255m',
    'purple': '\033[38;2;183;41;217m',
}


def _use_color() -> bool:
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.get('FORCE_COLOR'):
        return True
    return sys.stderr.isatty()


def _paint(kind: str, text: str, *, color: bool) -> str:
    if not color:
        return text
    return f'{_C[kind]}{text}{_C["reset"]}'


def _key(raw: str, *, color: bool) -> str:
    if raw.startswith('str:'):
        body = raw[4:]
        q = _paint('orange', '"', color=color)
        return f'{q}{_paint("green", body, color=color)}{q}'
    if raw.startswith('idx:'):
        return _paint('blue', raw[4:], color=color)
    if raw.startswith('attr:'):
        return '+' + _paint('white', raw[5:], color=color)
    return raw


def _scalar(node: DumpNode, *, color: bool) -> str:
    sk = node.scalar_kind
    if sk in {'None', 'bool'}:
        return _paint('orange', node.text, color=color)
    if sk in {'int', 'float'}:
        return _paint('blue', node.text, color=color)
    if sk == 'str':
        q = _paint('orange', '"', color=color)
        return f'{q}{_paint("green", node.text, color=color)}{q}'
    return _paint('green', node.text, color=color)


def format_node(
    node: DumpNode,
    *,
    depth: int = 0,
    color: bool = True,
    tip: str = '',
) -> str:
    pad = '  ' * depth
    child_pad = '  ' * (depth + 1)

    if node.kind in {'recursion', 'truncated'}:
        return _paint('gray', node.text, color=color) + tip

    if node.kind == 'scalar':
        return _scalar(node, color=color) + tip

    label = _paint('blue', node.label, color=color)
    if not node.children:
        return f'{label} []{tip}'

    lines = [f'{label} [{tip}']
    for key, child in node.children:
        lines.append(
            f'{child_pad}{_key(key, color=color)} => '
            f'{format_node(child, depth=depth + 1, color=color)}'
        )
    lines.append(f'{pad}]')
    return '\n'.join(lines)


def format_dump(
    *args,
    labels: list[str | None] | None = None,
    source: str | None = None,
    color: bool | None = None,
    skip_packages: tuple[str, ...] = (),
) -> str:
    if color is None:
        color = _use_color()
    if source is None:
        source = caller_frame(skip_packages=skip_packages)

    values = list(args)
    if not values:
        tip = f' {_paint("gray", f"// {source}", color=color)}' if source else ''
        return _paint('orange', '🐛', color=color) + tip

    if labels is None:
        labels = [None] * len(values)
    arg_names = caller_arg_names(skip_packages=skip_packages)

    blocks: list[str] = []
    for index, (label, value) in enumerate(zip(labels, values)):
        if label is None and index < len(arg_names):
            label = arg_names[index]
        tip_text = format_dump_tip(
            value,
            source=source,
            name=label,
            skip_packages=skip_packages,
        )
        tip = f' {_paint("gray", f"// {tip_text}", color=color)}' if tip_text else ''
        head = ''
        if label is not None:
            head = _paint('purple', str(label), color=color) + '\n'
        body = format_node(inspect_value(value), color=color, tip=tip)
        blocks.append(head + body)
    return '\n\n'.join(blocks)
