@echo off
echo Running DNS/DPI from Dragonfly CLI with Natlink.

set currentpath=%~dp0

TITLE Caster: Status Window
REM set PYTHONPATH=C:\Users\Leo\AppData\Local\caster\support_packages
cd "%currentpath%"
C:\Python38-32\python -m dragonfly load --engine natlink %~dp0_*.py --no-recobs-messages
REM C:\mc2\python -c "\n
REM import pywinauto" pywinauto -m dragonfly load --engine natlink _*.py --no-recobs-messages

pause 1
