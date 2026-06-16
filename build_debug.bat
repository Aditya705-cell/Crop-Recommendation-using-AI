@echo off
REM Crop Recommendation System - Build Script
REM This script automates APK building and installation

echo.
echo ===================================
echo Crop Recommendation App - Build Script
echo ===================================
echo.

REM Check if buildozer is installed
python -m pip show buildozer >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Buildozer...
    python -m pip install buildozer
)

REM Ensure Buildozer is patched for Python 3.14
python patch_buildozer.py

REM Build Debug APK
echo.
echo Building Debug APK...
echo.
buildozer android debug

if %errorlevel% equ 0 (
    echo.
    echo ===================================
    echo BUILD SUCCESSFUL!
    echo ===================================
    echo APK Location: bin\croprecommender-1.0-debug.apk
    echo.
    echo To install on device:
    echo   adb install bin\croprecommender-1.0-debug.apk
    echo.
) else (
    echo.
    echo BUILD FAILED!
    echo Check .buildozer logs for details
    echo.
    pause
)
