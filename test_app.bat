@echo off
REM Quick test script for the app

echo Testing Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Testing pip...
pip --version
if %errorlevel% neq 0 (
    echo ERROR: pip not found!
    pause
    exit /b 1
)

echo Upgrading pip and build tools...
python -m pip install --upgrade pip setuptools wheel

echo Installing dependencies...
pip install -r requirements.txt

echo Testing ML model...
python -c "from src.models.crop_model import CropRecommendationModel; m = CropRecommendationModel(); result = m.predict(50,40,30,25,65,6.5,150); print('✅ Model working!'); print('Primary crop:', result['primary_crop'])"

echo.
echo 🎉 Everything is working! Run 'python main.py' to start the app.
echo.
pause