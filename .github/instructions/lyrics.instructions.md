---
description: Format rules for lyric markdown files under lyrics/.
applyTo: "lyrics/**/*.md"
---

# Lyrics markdown format

These files are sources for the Jupyter Book site (`jupyter-book==1.0.3`).

## File structure

```markdown
# 艺术家名 <!-- omit in toc -->

- [曲名一](#曲名一)
- [曲名二](#曲名二)

## 曲名一

- 备注（剧/电影/动画 主题歌 etc., optional）
- https://www.uta-net.com/song/<id>/

歌词第一行<br>
歌词第二行<br>

第二段第一行<br>
第二段第二行<br>
```

## Rules

- Top-level `# Title` uses `<!-- omit in toc -->` to keep it out of the
  per-page TOC.
- Maintain the manual bullet TOC at the top of each file. When adding a song,
  insert a `- [题目](#题目)` line in alphabetical/release order matching the
  surrounding entries.
- Each song heading is `## ` (level 2). The anchor is auto-generated from the
  heading text — keep the bullet link in sync.
- Metadata bullets go immediately under the heading, before the lyrics.
  Prefer `https://www.uta-net.com/song/<id>/` as the source link.
- Lyric lines end with `<br>` (no trailing spaces). Stanzas are separated by
  one blank line, with no `<br>` on the blank line — `process_text.py` strips
  stray empty `<br>` entries.
- Preserve original Japanese punctuation (「」、。 ・ etc.). Do not transliterate
  or translate unless the user asks.
- Do not edit anything under `lyrics/_build/` — it is generated.
- When you create a brand-new chapter file (new artist/opus/type), also add a
  `- file: <folder>/<basename>` entry under the right `parts:` section in
  `lyrics/_toc.yml`.

See [.github/skills/add-song/SKILL.md](../skills/add-song/SKILL.md) for the
full procedure.
