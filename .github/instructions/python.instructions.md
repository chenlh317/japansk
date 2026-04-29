---
description: Conventions for Python scripts in this repo.
applyTo: "**/*.py"
---

# Python conventions

- Target Python 3.11+ (see `audioop-lts` shim in `requirements.txt`).
- Style: PEP 8, 4-space indent, double quotes, blank line between top-level
  blocks. Match the spacing style in `process_text.py` (blank lines inside
  functions to separate logical steps).
- Use `pathlib.Path` for filesystem paths, not `os.path` strings, when adding
  new code. Existing `os.walk` usage is fine — don't refactor unrelated code.
- Type-hint public functions and add Google-style docstrings:
  ```python
  def fn(arg: Path) -> None:
      """Short summary.

      Args:
          arg(Path): description
      Returns:
          None
      """
  ```
- Always open text files with `encoding="utf-8"`. Lyrics and metadata contain
  Japanese / Chinese characters.
- Lint locally with `flake8` before committing.
- Reuse helpers from `source/text_processor.py` rather than duplicating
  string-cleaning logic.
- Do not hardcode absolute Windows paths; read inputs from `videos.yaml`,
  `media_folders.txt`, or function arguments.
- New runtime dependencies must be added to `requirements.txt` with a
  compatible lower bound (`>=`). Do not bump `jupyter-book` past `1.0.3`.
