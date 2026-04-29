---
description: Run the local build (and optionally publish) for the lyrics Jupyter Book.
agent: agent
---

Walk the user through building (and optionally publishing) the lyrics site.

1. Confirm the venv at `.venv/` is activated (Windows: `.venv\Scripts\activate.bat`).
2. Run `python process_text.py` to normalize markdown.
3. Run `jb build lyrics`. Surface any warnings/errors.
4. Ask the user whether to publish. If yes, run:
   - `ghp-import -n -p -f lyrics/_build/html`
   - `git add . ; git commit -m "updates" ; git push origin main`
5. Otherwise stop after the local build and point at
   `lyrics/_build/html/index.html`.

The all-in-one Windows shortcut is `build_lyrics.bat`.

Never commit `lyrics/_build/` to `main`.
