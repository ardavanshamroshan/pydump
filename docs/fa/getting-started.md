# شروع سریع

دامپ ترمینال خوانا در کمتر از دو دقیقه.

## ۱. نصب

```bash
pip install pydump-dd
```

## ۲. اسکریپت

`main.py`:

```python
import pydump  # بعد از این dd/dump همه‌جا (شبیه Laravel)

user = {
    "id": 1,
    "name": "Ada",
    "roles": ["admin", "editor"],
}

dump(user)   # stderr، ادامه اجرا
```

## ۳. اجرا

```bash
python main.py
```

خروجی:

```text
dict:3 [
  "id" => 1
  "name" => "Ada"
  "roles" => list:2 [ ... ]
] // main.py:9
```

## ۴. دامپ و توقف

```python
dd(user)  # همان خروجی، سپس کد خروج 1
```

مثل `dd()` لاراول — بعد از inspect متوقف می‌شود.

!!! warning
    `dd()` باعث `SystemExit(1)` می‌شود. در production استفاده نکنید.

## ۵. import صریح (اختیاری)

```python
from pydump import dd, dump, render_text, configure
```

برای IDE و type checker بهتر است.

## گام بعد

- [امکانات](features.md)
- [مرجع API](api.md)
- [دمو](demo.md)
- [مستندات pydd](https://ardavanshamroshan.github.io/pydd/) — HTML برای وب

## لینک‌ها

| منبع | آدرس |
|------|------|
| PyPI | [pypi.org/project/pydump-dd](https://pypi.org/project/pydump-dd/) |
| GitHub | [github.com/ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump) |
