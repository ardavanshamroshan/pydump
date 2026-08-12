# pydump

Structured **dump and die** for Python scripts and CLIs. Stdlib only. No browser, no web framework required.

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Install**

    ---

    `pip install pydump-dd`

    [:octicons-arrow-right-24: Installation guide](installation.md)

-   :material-rocket-launch:{ .lg .middle } **Get started**

    ---

    Dump a dict in three lines.

    [:octicons-arrow-right-24: Getting started](getting-started.md)

-   :material-language-python:{ .lg .middle } **PyPI**

    ---

    Distribution name: **`pydump-dd`**

    [:octicons-link-external-24: pydump-dd on PyPI](https://pypi.org/project/pydump-dd/)

-   :material-github:{ .lg .middle } **GitHub**

    ---

    Source, issues, and contributions.

    [:octicons-link-external-24: ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump)

</div>

## Quick example

```python
import pydump  # installs dd/dump as builtins (Laravel-style)

user = {"id": 1, "name": "Ada", "roles": ["admin", "editor"]}
dump(user)   # stderr, keep running
dd(user)     # stderr, then exit 1
```

## Preview

```text
dict:3 [
  "id" => 1
  "name" => "Ada"
  "roles" => list:2 [
    0 => "admin"
    1 => "editor"
  ]
] // main.py:5
```

## Need HTML / web frameworks?

Use **[pydd](https://ardavanshamroshan.github.io/pydd/)** — pydump + HTML dumps for FastAPI, Flask, and Django.

| Need | Package | PyPI |
|------|---------|------|
| Terminal only | **pydump** | `pydump-dd` |
| Web apps | [pydd](https://ardavanshamroshan.github.io/pydd/) | `pydd-web` |

## License

MIT — see [GitHub repository](https://github.com/ardavanshamroshan/pydump).
