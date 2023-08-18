
# Manual

## Instruction

- Video
  1. Bookmark
  2. Download
  3. Archive to PC folder

- Audio
  1. Convert to mp3
  2. Format mp3 file
   - Artist
   - Album
   - File name
  3. Archive to PC folder
  4. Copy to mobile same folder
  5. Add to Muzio playlist

- Lyrics
  1. Find lyrics
  2. Add lyrics to this site
  3. Render and sync site

## Tools

- Video download: [You-get](https://you-get.org/)
- Text copy: Chrome plug-in
  - [Simple allow copy](https://chrome.google.com/webstore/detail/simple-allow-copy/aefehdhdciieocakfobpaaolhipkcpgc).
- Build: [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)
  - Command: `jb build lyrics`
- Deploy: [ghp-import](https://jupyterbook.org/en/stable/publish/gh-pages.html#option-2-automatically-push-your-build-files-with-ghp-import)
  - Command: `ghp-import -n -p -f lyrics/_build/html`
  - Then sync both `master` and `gh-pages` branches.
- Batch file
  - Run from Explorer `build_lyrics.bat`
  - From VSCode PowerShell: `cmd.exe -/c "build_lyrics.bat"`
- Publish: [GitHub Pages](https://pages.github.com/)
- Render PDF: `jb build lyrics/ --builder pdfhtml`
