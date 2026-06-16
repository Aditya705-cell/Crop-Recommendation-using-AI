#!/usr/bin/env bash
# Crop Recommendation System - Build Release Script (Linux/macOS)

echo ""
echo "==================================="
echo "Crop Recommendation App - Build Release"
echo "==================================="
echo ""

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Installing Buildozer..."
    pip install buildozer
fi

# Build Release APK
echo ""
echo "Building Release APK..."
echo ""
buildozer android release

if [ $? -eq 0 ]; then
    echo ""
    echo "==================================="
    echo "BUILD SUCCESSFUL!"
    echo "==================================="
    echo "APK Location: bin/croprecommender-1.0-release.apk"
    echo ""
else
    echo ""
    echo "BUILD FAILED!"
    echo "Check .buildozer logs for details"
    echo ""
fi
