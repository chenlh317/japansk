---
description: Jupyter Book configuration files.
applyTo: "lyrics/_toc.yml,lyrics/_config.yml"
---

# Jupyter Book config

- Pinned to `jupyter-book==1.0.3`. Do not introduce 2.x-only syntax.
- `_toc.yml` uses `format: jb-book` with `root: index` and `parts:` containing
  `chapters:` lists. Each chapter entry is `- file: <relative path without .md>`.
- Keep entries within a `parts:` group in the same alphabetical order as the
  surrounding entries unless the user specifies otherwise.
- After editing `_toc.yml`, ensure every referenced file exists under `lyrics/`.
