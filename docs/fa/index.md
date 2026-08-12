# pydump

**دامپ و توقف** ساختاریافته برای اسکریپت و CLI پایتون. فقط stdlib. بدون مرورگر و فریم‌ورک وب.

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **نصب**

    ---

    `pip install pydump-dd`

    [:octicons-arrow-right-24: راهنمای نصب](installation.md)

-   :material-rocket-launch:{ .lg .middle } **شروع سریع**

    ---

    دامپ یک dict در سه خط.

    [:octicons-arrow-right-24: شروع سریع](getting-started.md)

-   :material-language-python:{ .lg .middle } **PyPI**

    ---

    نام بسته: **`pydump-dd`**

    [:octicons-link-external-24: pydump-dd در PyPI](https://pypi.org/project/pydump-dd/)

-   :material-github:{ .lg .middle } **گیت‌هاب**

    ---

    سورس، issue و مشارکت.

    [:octicons-link-external-24: ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump)

</div>

## مثال سریع

```python
import pydump  # dd/dump به builtins (شبیه Laravel)

user = {"id": 1, "name": "Ada", "roles": ["admin", "editor"]}
dump(user)   # stderr، ادامه اجرا
dd(user)     # stderr، سپس خروج 1
```

## پیش‌نمایش

```text
dict:3 [
  "id" => 1
  "name" => "Ada"
  "roles" => list:2 [ ... ]
] // main.py:5
```

## HTML / فریم‌ورک وب می‌خواهید؟

**[pydd](https://ardavanshamroshan.github.io/pydd/)** — pydump + دامپ HTML برای FastAPI، Flask و Django.

| نیاز | بسته | PyPI |
|------|------|------|
| فقط ترمینال | **pydump** | `pydump-dd` |
| اپ وب | [pydd](https://ardavanshamroshan.github.io/pydd/) | `pydd-web` |

## مجوز

MIT — [مخزن گیت‌هاب](https://github.com/ardavanshamroshan/pydump).
