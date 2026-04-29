---
name: setup-environment
description: Bootstrap the local Python virtual environment.
---

# Skill: set up the dev environment

The repo expects a venv at `.venv/` (used by `build_lyrics.bat` and the
existing terminal sessions). Note: `lyrics/wiki/manual.md` mentions `venv/` —
the canonical path is `.venv/`.

## One-time setup (Windows)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notes

- Target Python 3.11+ (see `audioop-lts` shim in `requirements.txt`).
- `jupyter-book` must stay at `1.0.3`. Do not run `pip install -U jupyter-book`.
- `ffmpeg` is a native dependency (used by `pydub` / `slice_mp3.py`); install
  separately and add to PATH.
