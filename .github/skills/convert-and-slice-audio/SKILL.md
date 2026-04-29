---
name: convert-and-slice-audio
description: Convert downloaded videos to MP3 and optionally slice a segment.
---

# Skill: convert video → MP3 (and slice)

## Convert

`video_to_mp3.py` walks an input directory and writes a sibling `.mp3` for
every recognized video file.

- Default input dir: `./new` (set in the `__main__` block).
- Recognized extensions: `.mp4 .avi .mov .mkv .flv .rmvb .wmv .webm`.
- Output: same folder, same stem, `.mp3` at 320 kbps.
- Optional `start_end_time_dict` lets you trim a single video by mapping a
  `Path` to `(start_seconds, end_seconds)`.

To convert files currently in `raw_media/` instead of `new/`, change
`input_dir` in `__main__` (or call `convert_videos_to_mp3` directly) — do
**not** add a CLI argparse layer unless the user asks.

## Slice

`slice_mp3.py:slice_mp3_audio(song_path, start_second, end_second)` exports
`<stem>_<start>_<end>.mp3` next to the input. Edit the `__main__` block to
choose the file and times, then `python slice_mp3.py`.

Requires `ffmpeg` on PATH (e.g. `C:/ffmpeg-8.0-full_build/bin` on Windows).

## After slicing

Hand off to the [tag-mp3](../tag-mp3/SKILL.md) skill to set Artist / Album /
filename before archiving.
