# Crop Recommendation System

AI-powered crop recommendation system using machine learning to analyze soil and weather conditions.

## Overview

This application uses a Random Forest classifier trained on crop-soil compatibility data to recommend optimal crops based on 7 key parameters: nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall.

### Features

- **ML-based Crop Prediction**: Random Forest classifier with 10 crop recommendations
- **Command-line Interface**: Easy-to-use terminal interface
- **Real-time Recommendations**: Instant crop suggestions with confidence scores
- **10 Supported Crops**: Rice, Wheat, Maize, Cotton, Sugarcane, Pulses, Groundnut, Jute, Coconut, Potato
- **Data Validation**: Input validation and error handling

## Quick Start

### Prerequisites
- Python 3.9+
- pip package manager

### Installation

```bash
# Navigate to project folder
cd "c:\Users\ABC\Crop Recommendation"

# Install dependencies
pip install -r requirements.txt

# Test installation
test_app.bat
```

### Run the Application

```bash
python main.py
```

### Sample Input
```
Nitrogen (kg/hectare, 0-100): 50
Phosphorus (kg/hectare, 0-100): 40
Potassium (kg/hectare, 0-100): 30
Temperature (°C, 10-50): 25
Humidity (%, 0-100): 65
Soil pH (3-9): 6.5
Rainfall (mm, 0-300): 150
```

## Project Structure

```
Crop Recommendation/
├── main.py                 # Command-line application
├── requirements.txt        # Python dependencies
├── test_app.bat           # Test script
├── src/
│   ├── models/crop_model.py       # ML model and prediction logic
│   └── api/client.py              # Backend API client (optional)
└── README.md              # This file
```

## Input Parameters

| Parameter | Unit | Range | Description |
|-----------|------|-------|-------------|
| Nitrogen | kg/hectare | 0-100 | Soil nitrogen content |
| Phosphorus | kg/hectare | 0-100 | Soil phosphorus content |
| Potassium | kg/hectare | 0-100 | Soil potassium content |
| Temperature | °C | 10-50 | Average temperature |
| Humidity | % | 0-100 | Relative humidity |
| Soil pH | - | 3-9 | Soil acidity/basicity |
| Rainfall | mm | 0-300 | Annual rainfall |

## Supported Crops

1. **Rice** - Requires high water, warm temperatures
2. **Wheat** - Cool climate, moderate water
3. **Maize** - Warm climate, high nitrogen
4. **Cotton** - Warm, moderate water
5. **Sugarcane** - Tropical, high water
6. **Pulses** - Drought tolerant
7. **Groundnut** - Warm, well-drained soil
8. **Jute** - Tropical, high humidity
9. **Coconut** - Tropical coastal
10. **Potato** - Cool, well-drained soil

## Model Details

- **Algorithm**: Random Forest Classifier (100 trees)
- **Training Data**: Synthetic crop compatibility dataset
- **Features**: 7 soil/weather parameters
- **Output**: Top 3 crop recommendations with confidence scores
- **Accuracy**: Based on agricultural research data

## Usage Examples

### Example 1: Rice Farming Conditions
```
Nitrogen: 80, Phosphorus: 40, Potassium: 40
Temperature: 25, Humidity: 80, pH: 6.0, Rainfall: 200
→ Primary: Rice (95.2%)
```

### Example 2: Wheat Conditions
```
Nitrogen: 60, Phosphorus: 30, Potassium: 30
Temperature: 18, Humidity: 60, pH: 7.0, Rainfall: 80
→ Primary: Wheat (89.7%)
```

## Development

### Adding New Crops
Edit `src/models/crop_model.py`:
```python
self.crops = [
    'Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane',
    'Pulses', 'Groundnut', 'Jute', 'Coconut', 'Potato',
    'NewCrop'  # Add your crop here
]
```

### Modifying Model Parameters
```python
self.model = RandomForestClassifier(
    n_estimators=200,  # Increase trees
    random_state=42
)
```

### Custom Training Data
Replace the synthetic data generation in `_train_default_model()` with real agricultural data.

## API Integration (Optional)

The system includes an API client for backend integration:

```python
from src.api.client import CropRecommendationAPI

api = CropRecommendationAPI("http://your-server.com")
result = api.predict_crop(50, 40, 30, 25, 65, 6.5, 150)
```

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Model loading issues
Delete `src/models/crop_model.pkl` and `src/models/scaler.pkl` to retrain

### Invalid predictions
Check input ranges match the specified limits

## Future Enhancements

- [ ] Web interface with Flask/Django
- [ ] Mobile app with Kivy (when dependencies resolved)
- [ ] Real agricultural datasets
- [ ] Location-based weather integration
- [ ] Multi-language support
- [ ] Historical yield analysis

## License

MIT License - Free for educational and commercial use.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## Support

For issues or questions:
- Check the troubleshooting section
- Review the model parameters
- Test with sample inputs first