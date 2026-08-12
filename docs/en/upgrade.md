# Upgrade guide

How to upgrade **pydump-dd** safely.

## Current version

**0.2.4** — PyPI: [pydump-dd](https://pypi.org/project/pydump-dd/)

## Quick upgrade

```bash
pip install -U pydump-dd
```

With uv:

```bash
uv add "pydump-dd>=0.2.4"
```

## PyPI name change (0.2.2)

| Before | After |
|--------|-------|
| `pip install pydump` (conflicting name) | **`pip install pydump-dd`** |

**Import unchanged:** `import pydump`

Update dependencies:

```diff
- pydump>=0.2.1
+ pydump-dd>=0.2.4
```

If you use **pydd-web**, upgrading pydd pulls the matching pydump version automatically.

## 0.2.3 → 0.2.4

- Docs site + project URLs on PyPI metadata
- No code changes required

## 0.2.2 → 0.2.3

- README install docs fixed for PyPI name
- No code changes required

## 0.2.1 → 0.2.2

### Added
- `inspect_value` max-depth cap (default 4) — prevents hangs on large objects
- Dump tips: `$variable` names from AST; value kind and type alongside `file:line`
- MIT LICENSE file

### Changed
- PyPI distribution renamed to **`pydump-dd`**

### Action
Replace package name in `requirements.txt` / `pyproject.toml`. Reinstall:

```bash
pip uninstall pydump pydump-dd 2>/dev/null; pip install pydump-dd
```

## 0.2.0 → 0.2.1

### Added
- Laravel-style builtins via `import pydump`
- `install_helpers()` for explicit re-install
- Structured dumps for functions, methods, and classes

### Changed
- Tip placed on dump header line (after `[`), not after closing `]`
- Ruff/IDE documentation for builtin helpers

## 0.1.0 → 0.2.x

First feature-complete terminal release:

1. `pip install pydump-dd`
2. Replace `print(repr(x))` with `dump(x)` or `dd(x)`
3. Add `configure(project_root=...)` for cleaner tips

## Pinning versions

```toml
[project]
dependencies = ["pydump-dd>=0.2.4,<0.3"]
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: pydump` | Install **`pydump-dd`**, not `pydump` on PyPI |
| Hang on SQLAlchemy/large objects | Upgrade to >= 0.2.2 (max depth) |
| Tips missing `$variable` | Upgrade to >= 0.2.2 |
| Tip after `]` instead of header | Upgrade to >= 0.2.1 |

## Links

- [Changelog](changelog.md)
- [PyPI — pydump-dd](https://pypi.org/project/pydump-dd/)
- [GitHub releases](https://github.com/ardavanshamroshan/pydump/releases)
- [pydd upgrade guide](https://ardavanshamroshan.github.io/pydd/en/upgrade/)
