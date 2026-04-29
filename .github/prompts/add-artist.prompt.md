---
description: Create a new artist (or opus / type) chapter and register it in the TOC.
agent: agent
---

Create a new chapter page under `lyrics/` and wire it into `lyrics/_toc.yml`.

Inputs to collect:

1. Category: `by_artist`, `by_opus`, `by_type`, or `other`.
2. File basename (snake_case, romaji or pinyin), e.g. `yamaguchi_momoe`.
3. Display title for the `# Heading` (Japanese name, opus title, etc.).
4. Optional first song to seed the page.

Steps:

1. Verify `lyrics/<category>/<basename>.md` does not already exist.
2. Create the file with the standard skeleton:
   ```markdown
   # <display title> <!-- omit in toc -->

   ```
   If a first song was provided, add its TOC bullet and `## ` section per the
   lyrics format rules.
3. Edit `lyrics/_toc.yml`: add `- file: <category>/<basename>` under the
   matching `caption:` block, preserving the existing ordering.
4. Summarize the new file path and the TOC line added.

Reference: [.github/instructions/lyrics.instructions.md](../instructions/lyrics.instructions.md),
[.github/instructions/jupyter-book.instructions.md](../instructions/jupyter-book.instructions.md).
