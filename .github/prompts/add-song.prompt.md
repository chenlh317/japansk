---
description: Add a new song to an existing lyrics page.
agent: agent
---

You will add one new song to an existing file under `lyrics/by_artist/`,
`lyrics/by_opus/`, `lyrics/by_type/`, or `lyrics/other/`.

Inputs to collect from the user if not already provided:

1. Target file (e.g. `lyrics/by_artist/matsutoya_yumi.md`).
2. Song title (Japanese).
3. Optional metadata: drama/film/anime title, uta-net URL, etc.
4. Lyrics text (raw, line-broken).

Steps:

1. Read the target file to confirm it exists and inspect its current TOC and
   formatting style.
2. Insert a new `- [题目](#题目)` entry into the bullet TOC at the top, in the
   same ordering convention as the surrounding entries.
3. Append a new `## 题目` section at the bottom (or in matching order) with:
   - metadata bullets (drama/film/anime line if provided, then the source URL),
   - lyrics with `<br>` at the end of each line and blank lines between stanzas.
4. Do not add `<br>` on blank stanza-separator lines.
5. Show the user a summary of the change. Do **not** run `process_text.py` or
   `jb build` unless asked.

Follow [.github/instructions/lyrics.instructions.md](../instructions/lyrics.instructions.md)
and [.github/skills/add-song/SKILL.md](../skills/add-song/SKILL.md).
