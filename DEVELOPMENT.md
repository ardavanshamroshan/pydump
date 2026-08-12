# pydump — development guide

How `pydump` is built, how data flows through the code, and how to extend it.

## Package layout

```
src/pydump/
├── __init__.py    # public exports + install_helpers()
├── api.py         # dd, dump, render_text, configure, install_helpers
├── helpers.py     # builtins injection (Laravel-style globals)
├── core.py        # inspect_value, DumpNode, caller_frame
└── text.py        # ANSI formatter (terminal output)
```

## Design goals

1. **Framework-agnostic** — no imports from FastAPI, Flask, Django, or pygments
2. **One inspection pass** — `inspect_value()` produces a `DumpNode` tree reusable by other formatters (e.g. `pydd.html`)
3. **Terminal honesty** — print the full tree; do not emit collapse affordances (`▶` / `▼`) in text mode

## Data flow

```
value
  └─ inspect_value()     core.py — walk dict/list/set/object/scalar
       └─ DumpNode tree
            └─ format_node()   text.py — ANSI strings
                 └─ format_dump() → stderr (api.dump / api.dd)
```

### `DumpNode` (`core.py`)

| Field | Meaning |
|-------|---------|
| `kind` | `scalar`, `container`, `object`, `recursion` |
| `label` | Type label, e.g. `dict:4`, `list:3`, `MyClass` |
| `text` | Scalar body or recursion message |
| `scalar_kind` | `None`, `bool`, `int`, `float`, `str`, `other` |
| `children` | List of `(key_token, child_node)` — keys encoded as `str:name`, `idx:0`, `attr:field` |

### Inspection rules (`inspect_value`)

- **dict** — each key/value pair as children
- **list, tuple, set** — indexed children
- **function / method / builtin** — object node with `name`, `module`, `signature`, `file` when available
- **class** — object node with `module`, `bases`, public non-callable class attrs
- **objects** — public non-callable `__dict__` / `__slots__` attrs (names prefixed `attr:`)
- **scalars** — `None`, `bool`, `int`, `float`, `str` (truncated at 160 chars)
- **cycles** — `recursion` node when `id()` seen again

### Call-site detection (`caller_frame`)

`inspect.stack()` skips frames inside the `pydump` package. First user frame becomes `path:line`, relative to `project_root()` (defaults to `Path.cwd()`).

## Text formatter (`text.py`)

- Maps node kinds to ANSI 24-bit colors (orange structure, blue numbers/labels, green strings)
- Containers render as:

```text
dict:2 [ // demo.py:1
  "a" => 1
  "b" => 2
]
```

- No `max_depth` in terminal — all children rendered
- `format_dump()` joins multiple values with blank lines; kwargs get purple labels
- `// file:line` tip on first line after `[` (top-level only)

## Public API (`api.py`)

| Function | Behavior |
|----------|----------|
| `render_text` | `format_dump` + optional `color` / `source` / `skip_packages` |
| `dump` | `print(..., file=sys.stderr)` |
| `dd` | `dump` then `raise SystemExit(1)` |
| `configure` | sets `_PROJECT_ROOT` in `core.py` |
| `install_helpers` | inject `dd` / `dump` into builtins |

## Testing

```bash
cd pydump
uv sync --extra dev
uv run pytest -q
```

Tests live in `tests/test_pydump.py` — HTML-free smoke tests for render, dump, and exit code.

Companion manual project: `../testdump` (pip and uv install paths).

## Extending pydump

### New Python types

Add a branch in `inspect_value()` in `core.py`, return a `DumpNode` with appropriate `kind` and `children`.

### Custom terminal format

```python
from pydump import inspect_value

def my_format(value):
    node = inspect_value(value)
    # walk node.children recursively
```

Do not fork `inspect_value` in `pydd` — keep one source of truth in `pydump.core`.

### Custom colors

Edit `_C` and `_paint()` in `text.py`, or pass `color=False` and post-process `render_text()` output.

## Versioning and packaging

- Build backend: **hatchling**
- Package path: `src/pydump`
- Python: `>=3.10`
- Dependencies: none

## Changelog notes (0.1.0)

- Initial split from monolithic debug helper
- Full terminal expansion (no collapse markers)
- `DumpNode` shared with `pydd`
