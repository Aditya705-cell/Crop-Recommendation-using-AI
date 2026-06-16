@echo off
REM Crop Recommendation System - Build Release Script
REM This script builds a release APK for production deployment

echo.
echo ===================================
echo Crop Recommendation App - Build Release
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

REM Build Release APK
echo.
echo Building Release APK...
echo.
buildozer android release

if %errorlevel% equ 0 (
    echo.
    echo ===================================
    echo BUILD SUCCESSFUL!
    echo ===================================
    echo APK Location: bin\croprecommender-1.0-release.apk
    echo.
) else (
    echo.
    echo BUILD FAILED!
    echo Check .buildozer logs for details
    echo.
    pause
)
