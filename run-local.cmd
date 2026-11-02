@echo off
cd /d "%~dp0"
"%~dp0.python\python.exe" "%~dp0run.py" %*
if errorlevel 1 pause
