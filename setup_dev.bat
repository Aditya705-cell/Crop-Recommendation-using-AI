@echo off
REM Setup Development Environment

echo.
echo ===================================
echo Setting up Development Environment
echo ===================================
echo.

REM Install Python dependencies
echo Installing Python dependencies...
python -m pip install -r requirements.txt --upgrade

echo Installing Buildozer and Android tools...
python -m pip install buildozer cython

echo.
echo ===================================
echo Setup Complete!
echo ===================================
echo.
echo Next steps:
echo 1. Run 'python main.py' to test locally
echo 2. Run 'build_debug.bat' to create APK
echo.
echo For first-time APK build:
echo   buildozer android debug
echo   This will download Android SDK/NDK (may take 30+ minutes)
echo.
