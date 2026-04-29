# Copilot instructions — 日语学习相关资料收集整理

This repo collects Japanese-language learning material: song lyrics published as a
[Jupyter Book](https://jupyterbook.org/) site, plus Python utilities for
downloading videos, slicing audio, and post-processing markdown.

## Repo map

- `lyrics/` — Jupyter Book sources. Pinned to `jupyter-book==1.0.3`.
  - `_toc.yml`, `_config.yml` — book configuration. Update `_toc.yml` whenever a
    new chapter file is added.
  - `by_artist/`, `by_opus/`, `by_type/`, `other/` — chapter markdown files.
  - `wiki/manual.md` — usage notes.
  - `_build/` — generated output. **Do not edit by hand.** Published to the
    `gh-pages` branch by `ghp-import`.
- `source/text_processor.py` — helpers for cleaning markdown lyrics.
- `process_text.py` — batch entry point that walks `lyrics/` and applies the
  cleaners (special-character replacement, redundant `<br>` removal).
- `download_videos.py`, `video_to_mp3.py`, `slice_mp3.py`, `media_summary.py` —
  media pipeline scripts driven by `videos.yaml` / `media_folders.txt`.
- `build_lyrics.bat` — one-shot Windows build: activate venv → clean text →
  `jb build lyrics` → `ghp-import` → commit + push `main`.
- `raw_media/`, `new/` — local working folders, gitignored content.

## End-to-end workflow

The `lyrics/wiki/manual.md` page documents the human workflow. Mapped to
Copilot skills:

1. **Video** — download to `raw_media/` via
   [download-video](skills/download-video/SKILL.md) (yt-dlp directly or
   `download_videos.py` driven by `videos.yaml`).
2. **Audio** — extract / slice via
   [convert-and-slice-audio](skills/convert-and-slice-audio/SKILL.md), then
   tag via [tag-mp3](skills/tag-mp3/SKILL.md), and archive under
   `raw_media/<Artist>/`.
3. **Lyrics** — capture from uta-net via
   [find-lyrics](skills/find-lyrics/SKILL.md), insert via
   [add-song](skills/add-song/SKILL.md) (or
   [add-chapter](skills/add-chapter/SKILL.md) for a new artist/opus), then
   build & publish per [build-and-publish](prompts/build-and-publish.prompt.md).

The end-to-end orchestration lives in
[/add-from-youtube](prompts/add-from-youtube.prompt.md).

## Conventions

- **Python**: target 3.11+, follow PEP 8, format with the existing project
  style (4-space indent, double quotes, type hints + Google-style docstrings as
  in `process_text.py`). Lint with `flake8`.
- **Lyrics markdown** (files under `lyrics/`):
  - Each artist/opus file starts with `# 名字 <!-- omit in toc -->` followed by
    a manual TOC of `## ` song headings.
  - Every song section: `## 题目`, optional metadata bullets (drama/film,
    `https://www.uta-net.com/song/...`), then the lyrics.
  - Lyric lines end with `<br>` and stanzas are separated by a blank line.
  - Keep Japanese punctuation as-is; `process_text.py` normalizes a small set
    of special characters and strips empty `<br>` lines — do not duplicate that
    logic in edits.
  - When adding a song, also add it to the bullet TOC at the top of the file.
- **TOC**: when adding a brand-new chapter file, update `lyrics/_toc.yml`.
- **Dependencies**: pin compatible ranges in `requirements.txt`. Do not bump
  `jupyter-book` past `1.0.3` (see README — 2.x breaks the build).

## Build / publish

- Local build: `jb build lyrics` from repo root (venv active).
- Full publish on Windows: run `build_lyrics.bat`. It pushes generated HTML to
  `gh-pages` and source to `main`.
- Never commit anything inside `lyrics/_build/`.

## Working with Copilot in this repo

- Path-scoped guidance lives in `.github/instructions/`.
- Reusable task prompts live in `.github/prompts/` (e.g. add a song, add an
  artist, run the build).
- Two custom chat modes act as focused "agents":
  - **Lyrics Curator** — for editing `lyrics/` content.
  - **Media Pipeline** — for the Python download/transcode scripts.
- Recurring multi-step procedures are documented as skills in `.github/skills/`
  and referenced from the relevant instructions / chat modes.
