# نصب

## نام بسته

| توزیع PyPI | Import |
|------------|--------|
| **`pydump-dd`** | `import pydump` |

مستقل — بدون وابستگی وب.

## نصب پایه

```bash
pip install pydump-dd
```

## pip + venv

```bash
cd myapp
python -m venv .venv
source .venv/bin/activate
pip install pydump-dd
python main.py
```

## uv

```bash
uv add pydump-dd
```

```toml
[project]
dependencies = ["pydump-dd>=0.2.4"]
```

## نصب توسعه

```bash
git clone https://github.com/ardavanshamroshan/pydump.git
cd pydump
pip install -e ".[dev]"
```

## نیازمندی

- **پایتون** >= 3.10
- **وابستگی runtime:** هیچ (فقط stdlib)

## تأیید

```bash
python -c "import pydump; print(pydump.__version__)"
```

## اپ وب؟

```bash
pip install pydd-web
```

[مستندات pydd](https://ardavanshamroshan.github.io/pydd/).

## لینک‌ها

- **PyPI:** [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/)
- **GitHub:** [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump)
