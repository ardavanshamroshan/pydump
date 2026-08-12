# API Reference

## Public functions

| Function | Description |
|----------|-------------|
| `dump(*args, **kwargs)` | Write formatted dump to **stderr**, continue execution |
| `dd(*args, **kwargs)` | Same as `dump`, then `SystemExit(1)` |
| `render_text(*args, color=None, **kwargs)` | Return dump string; no I/O, no exit |
| `configure(project_root=...)` | Base path for relative `// file:line` tips |
| `install_helpers()` | Inject `dd` / `dump` into builtins (auto on `import pydump`) |

## Lower-level helpers

For custom formatters (used internally by pydd HTML):

| Symbol | Description |
|--------|-------------|
| `inspect_value(value)` | Walk a value → `DumpNode` tree |
| `DumpNode` | Dataclass representing one dump fragment |
| `set_project_root(path)` | Same as `configure` at module level |
| `caller_frame()` | Call-site frame for tip paths |
| `caller_arg_names()` | AST-inferred variable names from call line |
| `format_dump_tip(...)` | Build tip string: `file:line · $var · kind · type` |
| `describe_value(value)` | Human-readable kind/type metadata |
| `value_kind(value)` / `value_type_name(value)` | Type classification helpers |

## DumpNode schema

```python
@dataclass
class DumpNode:
    kind: str       # scalar | container | object | recursion | truncated
    label: str = ''
    text: str = ''
    scalar_kind: str = ''
    children: list[tuple[str, DumpNode]] = field(default_factory=list)
```

## Multiple values

```python
from pydump import dd

dd(post, request_id=42, user=current_user)
```

## Render without side effects

```python
from pydump import render_text

text = render_text({"ok": True}, color=False)
log.debug(text)
```

## Configure project root

```python
from pathlib import Path
from pydump import configure, dd

configure(project_root=Path(__file__).resolve().parent)
dd(some_value)  # tips like // app/views.py:88
```

## Editor and linter

After `import pydump`, builtins work at runtime but static tools need config.

### Ruff

```toml
[tool.ruff]
builtins = ["dd", "dump"]
```

### Type checkers

```python
from pydump import dd, dump
```

Or:

```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pydump import dd, dump
```

## Version

```python
import pydump
print(pydump.__version__)  # e.g. 0.2.4
```

## Links

- [PyPI — pydump-dd](https://pypi.org/project/pydump-dd/)
- [GitHub — pydump](https://github.com/ardavanshamroshan/pydump)
- [pydd API](https://ardavanshamroshan.github.io/pydd/en/api/)
