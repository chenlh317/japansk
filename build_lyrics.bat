
REM Format and build lyrics, and process with ghp-import

REM Run in VSCode terminal with below
REM cmd.exe -/c "build_lyrics.bat"


@REM python process_text.py

@REM jb build lyrics

@REM ghp-import -n -p -f lyrics/_build/html

git checkout main
git add .
git commit -m "batch file w git cmd"
git push origin main

git checkout gh-pages
git add .
git commit -m "sync pages"
git push origin gh-pages

git checkout main

cmd /k
