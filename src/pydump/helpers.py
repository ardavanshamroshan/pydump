"""Laravel-style global helpers via builtins."""

from __future__ import annotations

import builtins
from typing import Any, Callable


def install_helpers(
    *,
    dd: Callable[..., Any],
    dump: Callable[..., Any],
) -> None:
    """Inject ``dd`` / ``dump`` into builtins (no per-file import)."""
    builtins.dd = dd  # type: ignore[attr-defined]
    builtins.dump = dump  # type: ignore[attr-defined]
