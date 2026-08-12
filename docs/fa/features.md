# امکانات

## قابلیت‌های اصلی

- **بدون وابستگی** — فقط stdlib
- **ترمینال-first** — درخت کامل در log (بدون UI collapse)
- **ساختار خوانا** — `"key" => value` با برچسب نوع (`dict:3`, `list:2`)
- **tip محل فراخوانی** — `$variable · kind · type` و `// file:line`
- **رنگ ANSI** — وقتی stderr TTY است؛ `NO_COLOR` رعایت می‌شود
- **globals شبیه Laravel** — `import pydump` → `dd` / `dump` در builtins
- **چند مقدار** — positional و keyword جدا
- **سقف عمق** — پیش‌فرض 4؛ جلوگیری از hang روی object بزرگ
- **تشخیص cycle** — `<recursion TypeName>`
- **هسته مشترک** — همان `DumpNode` برای HTML [pydd](https://pypi.org/project/pydd-web/)

## چه چیز inspect می‌شود

| نوع | خروجی |
|-----|--------|
| dict | فرزند keyed، برچسب `dict:N` |
| list / tuple / set | فرزند indexed |
| class | module، bases، attributeهای public |
| function / method | نام، module، signature، فایل |
| instance | `__dict__` / `__slots__` public |
| scalar | None، bool، int، float، str (str تا 160 کاراکتر) |

## متغیر محیط

| متغیر | اثر |
|-------|-----|
| `NO_COLOR=1` | متن ساده |
| `FORCE_COLOR=1` | ANSI حتی بدون TTY |

## موارد استفاده

- اسکریپت و ابزار
- management command
- تست و notebook (مراقب `dd()`)
- log CI با `NO_COLOR=1`

## محدودیت‌ها

!!! warning
    - **بدون HTML** — [pydd](https://ardavanshamroshan.github.io/pydd/)
    - **`dd()` process را متوقف می‌کند**
    - **بدون syntax highlight**
    - **attribute خصوصی skip**
    - **عمق محدود**

## رابطه با pydd

```
pydump   → ترمینال
pydd     → pydump + HTML + فریم‌ورک
```

## لینک‌ها

| بسته | PyPI | مستندات |
|------|------|---------|
| pydump | [pydump-dd](https://pypi.org/project/pydump-dd/) | همین‌جا |
| pydd | [pydd-web](https://pypi.org/project/pydd-web/) | [pydd](https://ardavanshamroshan.github.io/pydd/) |
