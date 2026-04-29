---
description: Render the lyrics book as PDF.
agent: agent
---

Build the lyrics Jupyter Book in PDF mode.

Steps:

1. Confirm the venv at `.venv/` is active.
2. Run `jb build lyrics/ --builder pdfhtml`.
3. Surface any warnings/errors. The output lives under
   `lyrics/_build/pdf/` (or as reported by Jupyter Book).
4. Do **not** publish the PDF to `gh-pages` (only the HTML build is published
   by `ghp-import`).

Reference: `lyrics/wiki/manual.md` ("Render PDF").
