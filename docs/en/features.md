# Features

## Core capabilities

- **Zero dependencies** — stdlib only; easy to ship in any project
- **Terminal-first** — full tree expansion in logs (no fake collapse UI)
- **Readable structure** — `"key" => value` layout with typed labels (`dict:3`, `list:2`)
- **Call-site tips** — `$variable · kind · type` and `// file:line` on dump header
- **ANSI colors** — 24-bit colors when stderr is a TTY; respects `NO_COLOR`
- **Laravel-style globals** — `import pydump` injects `dd` / `dump` into builtins
- **Multiple values** — positional and keyword args each get a dump block
- **Max depth guard** — default depth 4 prevents hangs on huge objects (e.g. SQLAlchemy)
- **Cycle detection** — shows `<recursion TypeName>` for circular references
- **Shared core** — same `DumpNode` tree powers [pydd](https://pypi.org/project/pydd-web/) HTML output

## What gets inspected

| Value type | Output |
|------------|--------|
| dict | Keyed children, `dict:N` label |
| list / tuple / set | Indexed children, typed label |
| class | Module, bases, public attributes |
| function / method | Name, module, signature, source file |
| object instance | Public `__dict__` / `__slots__` (non-callable, no `_` prefix) |
| scalars | None, bool, int, float, str (str truncated at 160 chars) |

## Environment variables

| Variable | Effect |
|----------|--------|
| `NO_COLOR=1` | Plain text output |
| `FORCE_COLOR=1` | Force ANSI even when stderr is not a TTY |

## Use cases

- Scripts and one-off tools
- Management commands
- Tests and notebooks (careful with `dd()` — it exits)
- CI logs (`NO_COLOR=1` recommended)

## What pydump is not

!!! warning "Limitations"
    - **No HTML** — browser dumps require [pydd](https://ardavanshamroshan.github.io/pydd/)
    - **`dd()` stops the process** — not for production error handling
    - **No syntax highlighting** — colored text, not source-highlighted code
    - **Private attrs skipped** — by design on object instances
    - **Depth capped** — very deep structures show truncation markers

## Relationship to pydd

```
pydump   → terminal (this package)
pydd     → pydump + HTML + FastAPI / Flask / Django
```

Installing `pydd-web` automatically installs `pydump-dd`. For CLI-only projects, depend on `pydump-dd` directly.

## Links

| Package | PyPI | Docs |
|---------|------|------|
| pydump | [pydump-dd](https://pypi.org/project/pydump-dd/) | You are here |
| pydd | [pydd-web](https://pypi.org/project/pydd-web/) | [pydd docs](https://ardavanshamroshan.github.io/pydd/) |
