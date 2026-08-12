# Installation

## Package name

| PyPI distribution | Import |
|-------------------|--------|
| **`pydump-dd`** | `import pydump` |

Standalone — no web dependencies.

## Basic install

```bash
pip install pydump-dd
```

## pip + virtual environment

```bash
cd myapp
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pydump-dd
python main.py
```

## uv

```bash
cd myapp
uv add pydump-dd
uv run main.py
```

`pyproject.toml`:

```toml
[project]
dependencies = ["pydump-dd>=0.2.4"]
```

## Development install

```bash
git clone https://github.com/ardavanshamroshan/pydump.git
cd pydump
pip install -e ".[dev]"
uv run pytest -q
```

## Requirements

- **Python** >= 3.10
- **Runtime dependencies:** none (stdlib only)

## Verify installation

```bash
python -c "import pydump; print(pydump.__version__)"
```

## Web apps?

For FastAPI / Flask / Django HTML dumps, install **pydd** instead:

```bash
pip install pydd-web
```

See [pydd documentation](https://ardavanshamroshan.github.io/pydd/).

## Links

- **PyPI:** [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/)
- **GitHub:** [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump)
- **Issues:** [github.com/ardavanshamroshan/pydump/issues](https://github.com/ardavanshamroshan/pydump/issues)
