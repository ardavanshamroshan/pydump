# راهنمای ارتقا

ارتقای امن **pydump-dd**.

## نسخه فعلی

**0.2.4** — [pydump-dd](https://pypi.org/project/pydump-dd/)

## ارتقای سریع

```bash
pip install -U pydump-dd
```

## تغییر نام PyPI (0.2.2)

| قبل | بعد |
|-----|-----|
| `pip install pydump` | **`pip install pydump-dd`** |

**Import:** `import pydump`

```diff
+ pydump-dd>=0.2.4
```

با **pydd-web**، pydump خودکار به‌روز می‌شود.

## 0.2.3 → 0.2.4

- سایت مستندات + URLهای PyPI
- بدون تغییر کد

## 0.2.2 → 0.2.3

- مستندات نصب
- بدون تغییر کد

## 0.2.1 → 0.2.2

### اضافه
- سقف max-depth (پیش‌فرض 4)
- tip با `$variable` و kind/type
- LICENSE MIT

### تغییر
- نام PyPI: **`pydump-dd`**

## 0.2.0 → 0.2.1

- builtins Laravel-style
- dump ساختاریافته function/class
- tip روی header

## 0.1.0 → 0.2.x

1. `pip install pydump-dd`
2. `print(repr(x))` → `dump(x)`
3. `configure(project_root=...)`

## عیب‌یابی

| مشکل | راه‌حل |
|------|--------|
| `ModuleNotFoundError` | **`pydump-dd`** نصب کنید |
| hang روی object بزرگ | >= 0.2.2 |
| بدون `$variable` | >= 0.2.2 |

## لینک‌ها

- [تغییرات](changelog.md)
- [PyPI](https://pypi.org/project/pydump-dd/)
- [Releaseها](https://github.com/ardavanshamroshan/pydump/releases)
- [ارتقای pydd](https://ardavanshamroshan.github.io/pydd/fa/upgrade/)
