
REM Format and build lyrics, and process with ghp-import

REM Run in VSCode terminal with below
REM cmd.exe -/c "build_lyrics.bat"

REM Activate virtual environment
call .venv\Scripts\activate.bat

python process_text.py

jb build lyrics

REM ghp-import automatically pushes to gh-pages branch
ghp-import -n -p -f lyrics/_build/html

REM Commit and push source files from main branch
git add .
git commit -m "updates"
git push origin main

cmd /k
