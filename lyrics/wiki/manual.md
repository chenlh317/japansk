
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
  3. Archive to PC folders
  4. Copy to mobile same folders
  5. Add to mobile playlists

- Lyrics
  1. Find lyrics
  2. Add lyrics to this site
  3. Render and sync site
  4. URL: https://chenlh317.github.io/japansk/

## Tools

- Set up virtual environment:
  - `py -3.13 -m venv venv`
  - Activate on Windows: `venv\Scripts\activate`
  - Activate on macOS/Linux: `source venv/bin/activate`
  - Install dependencies: `pip install -r requirements.txt`
- Video download:
  - [yt-dlp](https://www.pythoncentral.io/yt-dlp-download-youtube-videos/)
    - [Pass cookies to yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp)
  - [You-get](https://you-get.org/)
  - [BiliBili Downloader](https://chromewebstore.google.com/detail/bilibili-downloader/hpblinpebjlcdcmpmfkbioliagcppmof)
  - `m3u8` files to (combined) `mp4`: `ffmpeg -i source_name.m3u8 -c copy target_name.mp4`
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
