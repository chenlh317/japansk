---
name: add-song
description: Step-by-step procedure to add one song to an existing lyrics chapter file.
---

# Skill: add a song to a lyrics chapter

Use when the user wants to append a single song to an existing file under
`lyrics/by_artist/`, `lyrics/by_opus/`, `lyrics/by_type/`, or `lyrics/other/`.

## Required inputs

| Field         | Example                                      |
| ------------- | -------------------------------------------- |
| Target file   | `lyrics/by_artist/matsutoya_yumi.md`         |
| Song title    | `あの日にかえりたい`                         |
| Metadata      | `家庭の秘密 主題歌`                          |
| Source URL    | `https://www.uta-net.com/song/335/`          |
| Lyrics body   | raw text, lines separated by `\n`            |

## Procedure

1. **Read** the target file. Note:
   - existing song ordering (release order vs alphabetical),
   - existing heading style (`## ` level 2),
   - whether stanzas use blank-line separation (they should).
2. **Section**: append (the page-level `{contents}` directive will pick up
   the new heading automatically — no manual TOC entry needed):
   ```markdown
   ## 题目

   - <metadata, if any>
   - <source URL, if any>

   <lyric line 1><br>
   <lyric line 2><br>

   <stanza 2 line 1><br>
   ```
   - Each lyric line ends with literal `<br>` and a newline.
   - Blank line between stanzas, with **no** `<br>` on the blank line.
   - Preserve original punctuation.
3. **Do not** run `process_text.py` or `jb build` unless explicitly asked.
4. Report back: file path and the new heading.

## Pitfalls

- Don't add the song to `_toc.yml` — only new chapter files go there.
- Don't transliterate or translate the lyrics.
- Don't strip Japanese punctuation; the cleaner only handles a small whitelist.
- Don't insert songs into anything under `lyrics/_build/`.
