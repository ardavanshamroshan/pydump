# دمو

مثال‌های قابل اجرا برای دامپ ترمینال.

## دامپ dict ساده

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

```bash
pip install pydump-dd
python debug.py
```

## dump and die

```python
from pydump import dd
dd({"status": "fatal"})  # چاپ، سپس exit 1
```

## چند مقدار

```python
dd(user, post, request_id=99)
```

## class و function

```python
dump(greet)
dump(User)
```

## متن ساده برای CI

```bash
NO_COLOR=1 python debug.py
```

## formatter سفارشی

```python
from pydump import inspect_value
node = inspect_value({"a": [1, 2, 3]})
# پیمایش node.children
```

[pydd](https://ardavanshamroshan.github.io/pydd/) HTML را همین‌طور می‌سازد.

## دمو وب

[دمو pydd](https://ardavanshamroshan.github.io/pydd/fa/demo/) برای FastAPI / Flask / Django.

## لینک‌ها

| منبع | آدرس |
|------|------|
| PyPI | [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/) |
| GitHub | [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump) |
