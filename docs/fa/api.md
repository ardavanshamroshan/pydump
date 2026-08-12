# مرجع API

## توابع عمومی

| تابع | توضیح |
|------|--------|
| `dump(*args, **kwargs)` | دامپ روی **stderr**، ادامه اجرا |
| `dd(*args, **kwargs)` | مثل `dump`، سپس `SystemExit(1)` |
| `render_text(*args, color=None, **kwargs)` | رشته دامپ؛ بدون I/O و exit |
| `configure(project_root=...)` | مسیر پایه tipهای `// file:line` |
| `install_helpers()` | تزریق `dd`/`dump` به builtins |

## helperهای سطح پایین

برای formatter سفارشی (pydd HTML):

| نماد | توضیح |
|------|--------|
| `inspect_value(value)` | value → درخت `DumpNode` |
| `DumpNode` | dataclass یک بخش دامپ |
| `caller_frame()` | فریم محل فراخوانی |
| `caller_arg_names()` | نام متغیر از AST |
| `format_dump_tip(...)` | رشته tip |
| `describe_value(value)` | metadata kind/type |

## چند مقدار

```python
dd(post, request_id=42, user=current_user)
```

## بدون side effect

```python
text = render_text({"ok": True}, color=False)
```

## project root

```python
configure(project_root=Path(__file__).resolve().parent)
```

## ویرایشگر

### Ruff

```toml
[tool.ruff]
builtins = ["dd", "dump"]
```

### Type checker

```python
from pydump import dd, dump
```

## نسخه

```python
import pydump
print(pydump.__version__)
```

## لینک‌ها

- [PyPI — pydump-dd](https://pypi.org/project/pydump-dd/)
- [GitHub — pydump](https://github.com/ardavanshamroshan/pydump)
- [API pydd](https://ardavanshamroshan.github.io/pydd/fa/api/)
