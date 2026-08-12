"""Public dump-and-die API — terminal only."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from pydump.core import caller_frame, set_project_root
from pydump.helpers import install_helpers as _install_helpers
from pydump.text import format_dump

__all__ = ['dd', 'dump', 'configure', 'render_text', 'install_helpers']


def configure(*, project_root: Path | str | None = None) -> None:
    """Set project root for relative // file:line tips."""
    set_project_root(project_root)


def render_text(
    *args: Any,
    color: bool | None = None,
    source: str | None = None,
    skip_packages: tuple[str, ...] = (),
    **kwargs: Any,
) -> str:
    """Build dump text without printing or exiting."""
    labels = [None] * len(args) + [str(k) for k in kwargs]
    values = list(args) + list(kwargs.values())
    if source is None:
        source = caller_frame(skip_packages=skip_packages)
    return format_dump(*values, labels=labels, color=color, source=source, skip_packages=skip_packages)


def dump(*args: Any, **kwargs: Any) -> None:
    """Print dump to stderr, keep running."""
    print(render_text(*args, **kwargs), file=sys.stderr)


def dd(*args: Any, **kwargs: Any) -> None:
    """Dump to stderr, then SystemExit(1)."""
    print(render_text(*args, **kwargs), file=sys.stderr)
    raise SystemExit(1)


def install_helpers() -> None:
    """Expose ``dd`` / ``dump`` as builtins (Laravel-style)."""
    _install_helpers(dd=dd, dump=dump)
