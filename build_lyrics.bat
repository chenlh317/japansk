
REM Format and build lyrics, and process with ghp-import

REM Run in VSCode terminal with cmd.exe -/c "build_lyrics.bat"


python process_text.py

jb build lyrics

ghp-import -n -p -f lyrics/_build/html

cmd /k
