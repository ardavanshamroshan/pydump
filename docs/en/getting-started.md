# Getting started

Get readable terminal dumps in under two minutes.

## 1. Install

```bash
pip install pydump-dd
```

## 2. Create a script

`main.py`:

```python
import pydump  # Laravel-style: dd/dump available everywhere after this

user = {
    "id": 1,
    "name": "Ada",
    "roles": ["admin", "editor"],
}

dump(user)   # print to stderr, keep running
```

## 3. Run

```bash
python main.py
```

Expected output:

```text
dict:3 [
  "id" => 1
  "name" => "Ada"
  "roles" => list:2 [
    0 => "admin"
    1 => "editor"
  ]
] // main.py:9
```

## 4. Dump and die

```python
dd(user)  # same output, then exit code 1
```

Use `dd()` when you want to stop after inspecting — like Laravel's `dd()`.

!!! warning
    `dd()` raises `SystemExit(1)`. Do not use in production request handlers.

## 5. Explicit imports (optional)

```python
from pydump import dd, dump, render_text, configure
```

Better for type checkers and IDEs.

## Next steps

- [Features](features.md) — full capability list
- [API Reference](api.md) — all public functions
- [Demo](demo.md) — more examples
- [pydd docs](https://ardavanshamroshan.github.io/pydd/) — HTML dumps for web apps

## Links

| Resource | URL |
|----------|-----|
| PyPI | [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/) |
| GitHub | [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump) |
