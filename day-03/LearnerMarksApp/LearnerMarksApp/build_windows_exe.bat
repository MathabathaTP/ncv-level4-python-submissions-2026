@echo off
cd /d "%~dp0"
py -m pip install --upgrade pyinstaller
if errorlevel 1 goto fail
py -m PyInstaller --noconfirm --clean --onefile --windowed --name LearnerMarksManager learner_marks_app.py
if errorlevel 1 goto fail
echo.
echo SUCCESS: dist\LearnerMarksManager.exe
pause
exit /b 0
:fail
echo Build failed. Check Python and internet connection.
pause
exit /b 1
