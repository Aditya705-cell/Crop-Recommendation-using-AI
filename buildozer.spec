[app]

# (str) Title of your application
title = Crop Recommendation

# (str) Package name
package.name = croprecommender

# (str) Package domain (needed for android/ios packaging)
package.domain = org.croprecommender

# (source.dir) Source directory (where the main.py is)
source.dir = .

# (list) Source include patterns (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Lists patterns for source files to exclude from the build
source.exclude_exts = pyc,pyo,.git,.gitignore,.github

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,src/*

# (list) Source files to include (let empty to include all the files)
source.include_files = 

# (list) Source files to exclude
source.exclude_dirs = tests,bin,.vscode,__pycache__

# (list) List of directory to exclude from the build
exclude_dirs = tests

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.2.1,numpy,scikit-learn,requests,pandas,pillow

# (str) Orientation of the application
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Supported orientation (landscape, portrait or all)
supported_orientations = portrait,landscape

# (bool) Indicate if the application should be icon only on the android homescreen
# icon_only = False

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy binary to libs_collections directory instead of libs
android.add_libs_armeabi_v7a = true
android.add_libs_armeabi = false
android.add_libs_x86 = false
android.add_libs_mips = false
android.add_libs_arm64_v8a = true

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup scheme (see documentation)
android.backup_policies = 

# (str) The Android logcat filters to use when running `buildozer osx logcat`
log_level = 2

# Display warning +/- timeout for buildozer to consider build as failed
warn_on_root = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning +/- timeout for building (in seconds)
warn_on_root = 1

# (str) Path to build directory where the built files are stored
build_dir = .buildozer

# (str) Path to build output (i.e. where the built files are)
bin_dir = ./bin
