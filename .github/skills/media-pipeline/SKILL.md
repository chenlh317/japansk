---
name: media-pipeline
description: How the download → transcode → slice → summarize media scripts fit together.
---

# Skill: media pipeline

The Python scripts at the repo root form a small pipeline that operates on
`raw_media/` and the lists in `videos.yaml` / `media_folders.txt`.

## Pieces

| Script               | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| `download_videos.py` | Reads `videos.yaml`; downloads via `yt-dlp` into `raw_media/`. |
| `video_to_mp3.py`    | Extracts MP3 audio from downloaded video files.             |
| `slice_mp3.py`       | Splits long MP3s based on chapter / silence detection.      |
| `media_summary.py`   | Produces a CSV/Excel summary of the local media folders.    |

All scripts assume the venv at `.venv/` is active and dependencies from
`requirements.txt` are installed (`yt-dlp`, `pydub`, `mutagen`, `eyed3`,
`pandas`, `openpyxl`, `pyarrow`, `audioop-lts`).

## When editing these scripts

- Read the script first; they are short and self-contained — match the existing
  style and CLI shape rather than introducing argparse/click/etc.
- Use `pathlib.Path` for new code; UTF-8 for text I/O.
- Do not hardcode absolute paths — read from `videos.yaml` or
  `media_folders.txt`.
- `raw_media/` content is local-only and gitignored. Don't add fixtures there.

## Common tasks

- **Add a video to download**: append a URL under `videos:` in `videos.yaml`.
- **Add a media folder to summarize**: append the folder path to
  `media_folders.txt`.
- **Run end-to-end**: `python download_videos.py` → `python video_to_mp3.py`
  → optional `python slice_mp3.py` → `python media_summary.py`.
