# Crop Recommendation System

A polished college project for intelligent farm planning, powered by machine learning and a modern web interface.

## What This Project Does

This project predicts the best crops to grow based on soil and weather conditions.
It supports both a local web UI and mobile/Kivy deployment, making it ideal for demos, presentations, and real-world testing.

## Key Features

- **ML-powered crop recommendation** using a Random Forest model
- **Web interface** with modern layout and image-backed results
- **Location-aware estimation** for humidity and soil values
- **Top 3 crop recommendations** with confidence scores
- **Clean presentation** for college demos and academic reporting
- **Multi-platform support**: web, command-line, and Kivy mobile app

## Technologies Used

- Python 3.9+
- Flask for the web interface
- Kivy for the mobile app UI
- scikit-learn for machine learning
- NumPy and Pandas for data processing
- Buildozer for Android APK packaging

## Getting Started

### 1. Install dependencies

```bash
cd "Crop Recommendation"
pip install -r requirements.txt
```

### 2. Run the web app

```bash
python web_app.py
```

Then open your browser at:

```text
http://127.0.0.1:5000
```

### 3. Run the desktop/mobile UI

```bash
python main.py
```

### 4. Run the command-line version

```bash
python main_cli.py
```

## Better Presentation Enhancements

- **Modern homepage** with hero section and feature cards
- **Improved form layout** with responsive styling
- **Crop image display** for recommended crops
- **Location-based auto-fill** for humidity and soil values
- **Polished result cards** ideal for demo walkthroughs

## APK Build (Android)

This repository includes a `buildozer.spec` file for Android packaging.

### Build the debug APK

```bash
buildozer android debug
```

Output file:

```text
bin/croprecommender-1.0-debug.apk
```

### Install on device

```bash
adb install bin/croprecommender-1.0-debug.apk
```

> On Windows, use an external terminal if VS Code fails to launch the integrated terminal.

## Project Structure

```
Crop Recommendation/
├── main.py                  # Kivy mobile app entry point
├── web_app.py               # Flask web application
├── main_cli.py              # Command-line version
├── buildozer.spec           # APK build config
├── requirements.txt         # Python dependencies
├── templates/               # Web page templates
├── static/                  # Web assets and styles
└── src/
    ├── models/
    │   └── crop_model.py    # Machine learning model
    ├── ui/
    │   └── screens.py       # Kivy UI layout
    └── api/
        └── client.py        # Optional backend client
```

## Input Parameters

The model uses these inputs:

| Parameter | Unit | Expected Range |
|-----------|------|----------------|
| Nitrogen | kg/hectare | 0–100 |
| Phosphorus | kg/hectare | 0–100 |
| Potassium | kg/hectare | 0–100 |
| Temperature | °C | 10–50 |
| Humidity | % | 0–100 |
| Soil pH | — | 3.0–9.0 |
| Rainfall | mm | 0–300 |

## Supported Crops

- Rice
- Wheat
- Maize
- Cotton
- Sugarcane
- Pulses
- Groundnut
- Jute
- Coconut
- Potato

## How It Works

1. User enters soil and weather values in the web UI or mobile app.
2. The app scales input values and passes them through the Random Forest model.
3. The model returns the top crop recommendation plus the top 3 alternatives.
4. The web page displays crop images and confidence scores.

## Customization

### Modify the model

Edit `src/models/crop_model.py` to update:
- crop labels
- training dataset
- model algorithm or hyperparameters

### Customize the web UI

Edit `templates/index.html` and `static/style.css` to change:
- page layout
- colors, buttons, and typography
- image cards and result presentation

### Customize the mobile UI

Edit `src/ui/screens.py` to adjust:
- input fields
- layout structure
- result view and interaction style

## Presentation Tips

- Use the web app to demo live predictions.
- Show how location detection auto-fills values.
- Highlight the top crop and image-backed recommendations.
- Point out the clean project structure and easy extension points.

## License

MIT License
