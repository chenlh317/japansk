---
description: End-to-end: download a YouTube video, extract MP3, find lyrics, add to the lyrics book.
agent: agent
---

Orchestrate the full Video → Audio → Lyrics workflow from `lyrics/wiki/manual.md`.

Inputs to collect from the user if not provided:

1. Video URL (YouTube, BiliBili, etc.).
2. Artist (Japanese).
3. Song title (Japanese).
4. Target lyrics file (e.g. `lyrics/by_artist/<artist>.md`). Offer to create
   it via the `add-chapter` skill if it doesn't exist.

Steps:

1. **Download** — follow [.github/skills/download-video/SKILL.md](../skills/download-video/SKILL.md).
   Prefer appending the URL to `videos.yaml` and running `download_videos.py`.
2. **Extract MP3** — follow [.github/skills/convert-and-slice-audio/SKILL.md](../skills/convert-and-slice-audio/SKILL.md).
   Ask whether a slice (start/end seconds) is needed.
3. **Tag** — follow [.github/skills/tag-mp3/SKILL.md](../skills/tag-mp3/SKILL.md).
   Confirm Artist / Album / Title before writing.
4. **Find lyrics** — follow [.github/skills/find-lyrics/SKILL.md](../skills/find-lyrics/SKILL.md).
   Prefer uta-net.com; capture the source URL.
5. **Insert** — follow [.github/skills/add-song/SKILL.md](../skills/add-song/SKILL.md).
   Update the per-page bullet TOC and append the `## ` section.
6. Ask whether to run `python process_text.py` and `jb build lyrics`. If yes,
   defer to the [build-and-publish](./build-and-publish.prompt.md) prompt.

Stop after each numbered step to confirm before moving on. Do not commit or
push automatically.
