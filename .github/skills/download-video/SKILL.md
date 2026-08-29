---
name: download-video
description: Download a video (e.g. from YouTube/BiliBili) into raw_media/ via yt-dlp or download_videos.py.
---

# Skill: download a video

Use when the user wants to fetch a video for the lyrics/media pipeline.

## Decide the path

- **Batch / repeatable**: append the URL under `videos:` in `videos.yaml`, then
  run `python download_videos.py`. Output goes to `./raw_media/` named
  `%(title)s [%(id)s].%(ext)s`.
- **One-off ad-hoc**: call `yt-dlp` directly. Standard recipe:
  ```
  yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 \
    -o "raw_media/%(title)s [%(id)s].%(ext)s" <video_url>
  ```
- **From `.m3u8`**: `ffmpeg -i index.m3u8 -c copy <name>.mp4`.

## Notes

- **YouTube requires the `deno` JS runtime** (used by `yt-dlp` + `yt-dlp-ejs`
  to solve JS challenges). If missing, downloads fail with misleading errors
  such as `This video is not available` — see
  [setup-environment](../setup-environment/SKILL.md) to install it. Keep
  `yt-dlp` up to date (`pip install -U yt-dlp`) when extraction breaks.
- `download_videos.py:clean_url` strips `&list=...` so playlist URLs become
  single-video URLs. Preserve that behavior if you edit it.
- For age-gated / member-only videos, pass cookies:
  `yt-dlp --cookies-from-browser chrome ...`
  (see https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp).
- `raw_media/` is gitignored — never commit downloaded media.
- Confirm with the user before downloading large playlists.

## After downloading

Hand off to the [convert-and-slice-audio](../convert-and-slice-audio/SKILL.md)
skill to extract MP3.
