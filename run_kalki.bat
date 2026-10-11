@echo off
title KALKI Assistant
cd /d "%~dp0"

echo Starting KALKI...
echo Project folder: %CD%
echo.

if exist ".venv312\Scripts\python.exe" (
    ".venv312\Scripts\python.exe" main.py
) else (
    py -3.12 main.py
)

echo.
echo KALKI stopped or an error occurred.
pause