# Building APK - Complete Guide

## Quick Start

### Windows Users
```bash
# Step 1: Setup environment (first time only)
setup_dev.bat

# Step 2: Test locally
python main.py

# Step 3: Build APK
build_debug.bat
```

### Linux/macOS Users
```bash
# Step 1: Setup environment (first time only)
chmod +x setup_dev.sh
./setup_dev.sh

# Step 2: Test locally
python main.py

# Step 3: Build APK
chmod +x build_debug.sh
./build_debug.sh
```

## Prerequisites

### 1. Python 3.9+
- **Windows**: Download from python.org
- **macOS**: `brew install python@3.11`
- **Linux**: `apt install python3.11 python3.11-dev`

### 2. Java Development Kit (JDK)
- Install JDK 8 or later (required for Android SDK)
- Buildozer will guide you through setup

### 3. Buildozer
```bash
pip install buildozer cython
```

## Build Process

### First-Time Setup (30-60 minutes)
The first APK build downloads Android SDK/NDK and tools:

```bash
buildozer android debug
```

Buildozer will:
1. Check for Java (JDK)
2. Download Android SDK tools
3. Download NDK
4. Build the APK

### Subsequent Builds (5-15 minutes)
Once setup is complete, rebuilds are faster:

```bash
buildozer android debug
```

## Build Outputs

### Debug APK
- **Location**: `bin/croprecommender-1.0-debug.apk`
- **Size**: ~50-100 MB
- **Usage**: Testing on devices/emulators
- **Install**: `adb install bin/croprecommender-1.0-debug.apk`

### Release APK
- **Location**: `bin/croprecommender-1.0-release.apk`
- **Size**: ~50-100 MB (optimized)
- **Usage**: Production deployment, app stores
- **Build**: `buildozer android release`

## Installation on Device

### Android Physical Device
1. Enable Developer Mode: Settings → About → Build Number (tap 7 times)
2. Enable USB Debugging: Settings → Developer Options → USB Debugging
3. Connect device via USB
4. Install: `adb install bin/croprecommender-1.0-debug.apk`

### Android Emulator
1. Start Android emulator
2. Install: `adb install bin/croprecommender-1.0-debug.apk`

## Troubleshooting

### "Java command not found"
- **Solution**: Install JDK 8+
  - Windows: Download from oracle.com
  - macOS: `brew install openjdk`
  - Linux: `apt install openjdk-11-jdk`

### "buildozer: command not found"
- **Solution**: 
  ```bash
  pip install buildozer
  ```

### Build Fails with "AAPT Error"
- **Solution**: Update Android SDK
  ```bash
  buildozer android update
  ```

### "gradle build" fails
- **Solution**: Clear build cache
  ```bash
  buildozer android clean
  buildozer android debug
  ```

### Slow Build
- Ensure SSD (not HDD) for build directory
- Close unnecessary applications
- First build is always slower

## Configuration

### Edit buildozer.spec to customize:
- **App name**: Change `title = Crop Recommendation`
- **Package**: Change `package.name = croprecommender`
- **Permissions**: Add/remove in `android.permissions`
- **Target API**: Edit `android.api = 31`
- **Architecture**: Edit `android.archs = arm64-v8a,armeabi-v7a`

### Common Customizations

**Change App Icon**
```
icon.filename = %(source.dir)s/assets/icon.png
```

**Change Splash Screen**
```
presplash.filename = %(source.dir)s/assets/presplash.png
```

**Add Permissions**
```
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,ACCESS_FINE_LOCATION
```

## Advanced Options

### Build for Specific Architecture
```bash
# ARM64 only (modern phones)
buildozer android debug -a arm64_v8a

# 32-bit only
buildozer android debug -a armeabi_v7a
```

### Enable Advanced Features
Edit `buildozer.spec`:
```ini
# Enable camera
android.permissions = CAMERA

# Enable GPS
android.permissions = ACCESS_FINE_LOCATION

# Enable network
android.permissions = INTERNET,ACCESS_NETWORK_STATE
```

## Building Release APK

### Create Keystore (first time only)
```bash
keytool -genkey -v -keystore my-key.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias my-key
```

### Configure buildozer.spec
```ini
android.release_artifact = apk
android.keystore = 1
android.keystore_path = my-key.keystore
android.keystore_alias = my-key
```

### Build Release
```bash
buildozer android release
```

## Performance Optimization

### Reduce APK Size
1. Use ARM64 only architecture
2. Remove unused libraries
3. Enable ProGuard minification

### Faster Build Times
1. Use SSD for build directory
2. Increase RAM allocation
3. Pre-download SDK/NDK

## Support & Resources

- **Kivy Documentation**: https://kivy.org/doc/stable/
- **Buildozer**: https://buildozer.readthedocs.io/
- **Android SDK**: https://developer.android.com/
- **Stack Overflow**: Tag with `kivy` and `buildozer`

## Testing

### Before Building APK
1. Test locally: `python main.py`
2. Check all features work
3. Test with sample data

### After Building APK
1. Install on test device
2. Verify app launches
3. Test crop prediction
4. Check performance

## Next Steps

1. ✅ Complete project structure created
2. ✅ All dependencies configured
3. **Run setup script** (setup_dev.bat or setup_dev.sh)
4. **Test locally** (python main.py)
5. **Build APK** (build_debug.bat or build_debug.sh)
6. **Install on device** (adb install)
7. **Deploy** to app store (release build)
