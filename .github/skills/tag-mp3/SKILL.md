---
name: tag-mp3
description: Set Artist / Album / Title metadata and rename MP3 files for archive.
---

# Skill: tag and rename MP3 files

The manual workflow's "Format mp3 file" step. Use after
[convert-and-slice-audio](../convert-and-slice-audio/SKILL.md).

## Required inputs

| Field    | Example                |
| -------- | ---------------------- |
| Artist   | `松任谷由実`           |
| Album    | `Album / single name`  |
| Title    | `あの日にかえりたい`   |
| File     | path to the `.mp3`     |

## Conventions

- Keep Japanese characters in tags and filenames; UTF-8 throughout.
- File name pattern: `<Title>.mp3` (one song per file). The artist/album live
  in the ID3 tags, not the filename.
- Final archive folder: `raw_media/<Artist>/` (matches the existing
  `raw_media/久保田早紀/`, `raw_media/松任谷由実/` etc.).

## Snippet (mutagen)

```python
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def tag_mp3(path: Path, artist: str, album: str, title: str) -> None:
    """Write basic ID3 tags to an MP3 file."""
    audio = MP3(path, ID3=EasyID3)
    if audio.tags is None:
        audio.add_tags()
    audio["artist"] = artist
    audio["album"] = album
    audio["title"] = title
    audio.save()
```

`eyed3` is also available if the user prefers it.

## Pitfalls

- Don't overwrite existing tags without confirming.
- Don't move files into `raw_media/<Artist>/` automatically — confirm first.
