#!/usr/bin/env bash
# Crop Recommendation System - Setup Development Environment (Linux/macOS)

echo ""
echo "==================================="
echo "Setting up Development Environment"
echo "==================================="
echo ""

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt --upgrade

echo "Installing Buildozer and Android tools..."
pip install buildozer cython

echo ""
echo "==================================="
echo "Setup Complete!"
echo "==================================="
echo ""
echo "Next steps:"
echo "1. Run 'python main.py' to test locally"
echo "2. Run './build_debug.sh' to create APK"
echo ""
echo "For first-time APK build:"
echo "  buildozer android debug"
echo "  This will download Android SDK/NDK (may take 30+ minutes)"
echo ""
