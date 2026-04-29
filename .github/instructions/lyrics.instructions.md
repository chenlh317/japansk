---
description: Format rules for lyric markdown files under lyrics/.
applyTo: "lyrics/**/*.md"
---

# Lyrics markdown format

These files are sources for the Jupyter Book site (`jupyter-book==1.0.3`).

## File structure

````markdown
# 艺术家名

```{contents}
:depth: 3
```

## 曲名一

- 备注（剧/电影/动画 主题歌 etc., optional）
- https://www.uta-net.com/song/<id>/

歌词第一行<br>
歌词第二行<br>

第二段第一行<br>
第二段第二行<br>
````

## Rules

- Top-level `# Title` is followed by a Jupyter Book `{contents}` directive
  that auto-generates the per-page TOC. Do **not** add a manual bullet TOC.
- Each song heading is `## ` (level 2). The `{contents}` directive picks them
  up automatically — no need to maintain anchor links by hand.
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
