# Demo

Runnable examples for terminal dumps.

## Basic dict dump

`debug.py`:

```python
import pydump

payload = {
    "id": 1,
    "author": "Jane Doe",
    "title": "Hello world",
    "tags": ["python", "debug", "pydump"],
}

dump(payload)
```

Run:

```bash
pip install pydump-dd
python debug.py
```

Output:

```text
dict:4 [
  "id" => 1
  "author" => "Jane Doe"
  "title" => "Hello world"
  "tags" => list:3 [
    0 => "python"
    1 => "debug"
    2 => "pydump"
  ]
] // debug.py:12
```

## Dump and die

```python
from pydump import dd

dd({"status": "fatal", "code": 42})
# prints dump, then process exits with code 1
```

## Multiple values

```python
from pydump import dd

user = {"id": 1}
post = {"title": "Hello"}
dd(user, post, request_id=99)
```

Each value gets its own dump block with separate tips.

## Class and function introspection

```python
from pydump import dump

def greet(name: str) -> str:
    return f"Hello, {name}"

class User:
    id: int = 1
    name: str = "Ada"

dump(greet)
dump(User)
```

Shows name, module, signature, bases, and public attributes.

## Plain text for CI

```bash
NO_COLOR=1 python debug.py
```

Or in code:

```python
from pydump import render_text
print(render_text(data, color=False))
```

## Custom formatter (advanced)

Build on the shared inspection core:

```python
from pydump import inspect_value, DumpNode

node = inspect_value({"a": [1, 2, 3]})

def walk(n: DumpNode, indent=0):
    print("  " * indent + n.label)
    for key, child in n.children:
        print("  " * indent + f"{key}:")
        walk(child, indent + 1)

walk(node)
```

This is how [pydd](https://ardavanshamroshan.github.io/pydd/) builds HTML output.

## Web demo

For FastAPI / Flask / Django HTML dumps, see [pydd demo](https://ardavanshamroshan.github.io/pydd/en/demo/).

## Links

| Resource | URL |
|----------|-----|
| PyPI | [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/) |
| GitHub | [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump) |
