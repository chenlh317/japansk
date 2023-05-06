
REM Build lyrics and process with ghp-import

jb build lyrics

ghp-import -n -p -f lyrics/_build/html

cmd /k