#!/usr/bin/env bash
# Crop Recommendation System - Build Script (Linux/macOS)

echo ""
echo "==================================="
echo "Crop Recommendation App - Build Script"
echo "==================================="
echo ""

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Installing Buildozer..."
    pip install buildozer
fi

# Build Debug APK
echo ""
echo "Building Debug APK..."
echo ""
buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "==================================="
    echo "BUILD SUCCESSFUL!"
    echo "==================================="
    echo "APK Location: bin/croprecommender-1.0-debug.apk"
    echo ""
    echo "To install on device:"
    echo "  adb install bin/croprecommender-1.0-debug.apk"
    echo ""
else
    echo ""
    echo "BUILD FAILED!"
    echo "Check .buildozer logs for details"
    echo ""
fi
