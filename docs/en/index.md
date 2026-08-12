# pydump

Structured **dump and die** for Python scripts and CLIs. Stdlib only. No browser, no web framework required.

<figure class="shot" markdown>
![pydump terminal dump](../assets/images/pydump-dd-hero.jpg)
<figcaption>Rich terminal trees — ANSI colors when stderr is a TTY</figcaption>
</figure>

## Stack

Built for plain Python. Need HTML in the browser? Use [pydd](https://ardavanshamroshan.github.io/pydd/).

<div class="grid cards fw-cards" markdown>

-   [![Python](../assets/logos/python.svg){ .fw-logo }](getting-started.md)

    **[Python / CLI](getting-started.md)**

    Stdlib only — scripts, tests, CI

-   [![pydd](../assets/images/pydd-logo-mark.png){ .fw-logo }](https://ardavanshamroshan.github.io/pydd/)

    **[Need web? → pydd](https://ardavanshamroshan.github.io/pydd/)**

    FastAPI · Flask · Django HTML dumps

</div>

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Install**

    ---

    `pip install pydump-dd`

    [:octicons-arrow-right-24: Installation guide](installation.md)

-   :material-rocket-launch:{ .lg .middle } **Get started**

    ---

    Dump a dict in three lines.

    [:octicons-arrow-right-24: Getting started](getting-started.md)

-   :material-language-python:{ .lg .middle } **PyPI**

    ---

    Distribution name: **`pydump-dd`**

    [:octicons-link-external-24: pydump-dd on PyPI](https://pypi.org/project/pydump-dd/)

-   :material-github:{ .lg .middle } **GitHub**

    ---

    Source, issues, and contributions.

    [:octicons-link-external-24: ardavanshamroshan/pydump](https://github.com/ardavanshamroshan/pydump)

</div>

## Quick example

```python
import pydump  # installs dd/dump as builtins

user = {"id": 1, "name": "Ada", "roles": ["admin", "editor"]}
dump(user)   # stderr, keep running
dd(user)     # stderr, then exit 1
```

## Live preview

<figure class="shot" markdown>
![Terminal dump hero](../assets/images/pydump-dd-hero.jpg)
<figcaption>Fully expanded trees — no collapse UI in the terminal</figcaption>
</figure>

<figure class="shot" markdown>
![Dict dump panel](../assets/images/pydump-dd-panel.jpg)
<figcaption>Typed header, nested lists, `// file:line` tip</figcaption>
</figure>

<figure class="shot" markdown>
![Close-up dict dump](../assets/images/pydump-dd-dict-result.jpg)
<figcaption>dict / list trees with syntax colors</figcaption>
</figure>

## Need HTML / web frameworks?

Use **[pydd](https://ardavanshamroshan.github.io/pydd/)** — pydump + HTML dumps for FastAPI, Flask, and Django.

| Need | Package | PyPI |
|------|---------|------|
| Terminal only | **pydump** | `pydump-dd` |
| Web apps | [pydd](https://ardavanshamroshan.github.io/pydd/) | `pydd-web` |

## License

MIT — see [GitHub repository](https://github.com/ardavanshamroshan/pydump).
