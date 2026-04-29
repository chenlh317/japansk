---
name: add-chapter
description: Create a new artist/opus/type chapter file and register it in _toc.yml.
---

# Skill: add a new chapter to the lyrics book

Use when the target page does not yet exist (new artist, new opus, new type).

## Required inputs

| Field      | Example                                            |
| ---------- | -------------------------------------------------- |
| Category   | `by_artist` \| `by_opus` \| `by_type` \| `other`   |
| Basename   | `yamaguchi_momoe` (snake_case, no extension)       |
| Heading    | `山口百恵`                                         |

## Procedure

1. Verify `lyrics/<category>/<basename>.md` does not exist.
2. Create the file with this skeleton (no trailing whitespace):
   ```markdown
   # <heading> <!-- omit in toc -->

   ```
3. Open `lyrics/_toc.yml` and add a line under the matching `caption:` block:
   ```yaml
       - file: <category>/<basename>
   ```
   Preserve the existing ordering inside the block.
4. If the user supplied a first song, hand off to the `add-song` skill before
   summarizing.
5. Report: new file path + the TOC line that was added.

## Pitfalls

- The TOC entry is path-relative to `lyrics/` and has **no** `.md` suffix.
- Don't introduce `format: jb-book` 2.x syntax — pinned to 1.0.3.
- Don't reorder unrelated entries in `_toc.yml`.
