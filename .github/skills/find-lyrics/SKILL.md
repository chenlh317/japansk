---
name: find-lyrics
description: Locate Japanese song lyrics from a trusted source and prepare them for add-song.
---

# Skill: find lyrics for a song

The fuzzy "Find lyrics" step from the manual workflow.

## Preferred sources (in order)

1. **uta-net.com** — canonical for this repo. URL pattern:
   `https://www.uta-net.com/song/<id>/`. Save the URL as the source bullet.
2. **utamap.com**, **j-lyric.net** — acceptable fallbacks. Still record the URL.
3. Avoid pasting from auto-generated subtitles or fan blogs unless the user
   confirms — accuracy varies.

## What to capture

- Song title in original kanji/kana.
- Source URL.
- Optional: drama / film / anime tie-in (one bullet line above the URL).
- Lyrics body, stanzas separated by blank lines.

## Cleaning before insert

- Preserve original Japanese punctuation (「」、。 ・).
- Strip leading/trailing whitespace from lines.
- Do **not** translate or transliterate.
- Do **not** add `<br>` here — the [add-song](../add-song/SKILL.md) skill
  appends `<br>` and writes the file.

## Hand off

Pass the captured fields straight into the
[add-song](../add-song/SKILL.md) skill.

## Pitfalls

- Some pages disable copy. The Chrome plug-in *Simple Allow Copy* is the
  documented workaround in `lyrics/wiki/manual.md`.
- Don't fabricate lyrics — if a source can't be reached, ask the user to paste
  the lyrics directly.
