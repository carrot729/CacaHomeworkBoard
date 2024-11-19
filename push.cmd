@echo off
git.exe add .
git.exe commit -m "%DATE%_%TIME%"
echo pushing......
git.exe push origin homework-pages
echo done
