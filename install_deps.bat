@echo off
REM Alternative Kivy installation script

echo Installing Kivy dependencies first...
pip install kivy-deps.angle
pip install kivy-deps.glew
pip install kivy-deps.sdl2

echo Installing Kivy...
pip install kivy

echo Installing other dependencies...
pip install numpy scikit-learn pandas pillow requests

echo Installation complete!
pause