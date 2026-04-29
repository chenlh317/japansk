---
description: Format rules for the media pipeline input lists.
applyTo: "videos.yaml,media_folders.txt"
---

# Media pipeline inputs

## `videos.yaml`

- Top-level key is `videos:` containing a YAML list of URLs.
- One URL per list item, prefixed with `- `.
- Playlist suffixes (`&list=...`) are tolerated — `download_videos.py:clean_url`
  strips them at runtime. Keep the URL as the user pasted it unless asked.
- Add new entries at the bottom; do not reorder existing entries.
- File is UTF-8, LF or CRLF both fine.

## `media_folders.txt`

- One folder path per line.
- Absolute paths are OK (this file is local-only).
- Blank lines and `#`-prefixed comments are allowed.
- Do not commit personal absolute paths if the file becomes shared.
