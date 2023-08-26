
REM Format and build lyrics, and process with ghp-import

REM Run in VSCode terminal with below
REM cmd.exe -/c "build_lyrics.bat"


python process_text.py

jb build lyrics

ghp-import -n -p -f lyrics/_build/html

git checkout main
git add .
git commit -m "updates"
git push origin main

git checkout gh-pages
git add .
git commit -m "sync pages"
git push origin gh-pages

git checkout main

cmd /k
