# Changelog

All notable changes to **pydump-dd** are documented here.

## [0.2.4] - 2026-08-12

### Added
- Bilingual documentation site (English + فارسی) on GitHub Pages

### Changed
- Project URLs: Homepage / Documentation → https://ardavanshamroshan.github.io/pydump/
- README links to docs, PyPI, and GitHub

## [0.2.3] - 2026-08-12

### Fixed
- README install docs: use PyPI package `pydump-dd` instead of local path

## [0.2.2] - 2026-08-12

### Added
- `inspect_value` max-depth cap (default 4) to avoid hangs on large objects (e.g. SQLAlchemy results)
- Dump tips: infer `$variable` names from `dd(...)` call site; show value kind and type alongside `file:line`
- MIT `LICENSE` file

### Changed
- PyPI distribution renamed to **`pydump-dd`** (`import pydump` unchanged)

## [0.2.1] - 2026-07-23

### Added
- Laravel-style global helpers: `import pydump` injects `dd` / `dump` into builtins
- `install_helpers()` to re-install builtins explicitly

### Changed
- Document Ruff `builtins = ["dd", "dump"]` and IDE import caveats
- `// file:line` tip placed on dump header line (after `[`), not after closing `]`
- `render_text(..., skip_packages=...)` for call-site tip filtering
- Functions, methods, and classes dump as structured objects (name, signature, module, bases)

## [0.2.0] - 2026-07-23

### Notes
- Tag/release `v0.2.0` on GitHub; superseded by `v0.2.1`

## [0.1.0] - 2026-07-22

### Added
- Initial release: terminal `dd` / `dump` / `render_text`

---

[0.2.4]: https://github.com/ardavanshamroshan/pydump/releases/tag/v0.2.4
[0.2.3]: https://github.com/ardavanshamroshan/pydump/releases/tag/v0.2.3
[0.2.2]: https://github.com/ardavanshamroshan/pydump/releases/tag/v0.2.2
[0.2.1]: https://github.com/ardavanshamroshan/pydump/releases/tag/v0.2.1

See also: [Upgrade guide](upgrade.md) · [PyPI](https://pypi.org/project/pydump-dd/) · [GitHub](https://github.com/ardavanshamroshan/pydump)
