from flask import Flask, render_template, request, jsonify
from src.models.crop_model import CropRecommendationModel
import json
import urllib.request

app = Flask(__name__)
model = CropRecommendationModel()



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None, values={}, error=None)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = {
            'nitrogen': request.form.get('nitrogen', ''),
            'phosphorus': request.form.get('phosphorus', ''),
            'potassium': request.form.get('potassium', ''),
            'temperature': request.form.get('temperature', ''),
            'humidity': request.form.get('humidity', ''),
            'ph': request.form.get('ph', ''),
            'rainfall': request.form.get('rainfall', ''),
        }

        inputs = [float(values[k]) for k in values]
        result = model.predict(*inputs)

        if not result['success']:
            return render_template('index.html', result=None, values=values, error=result.get('error', 'Prediction failed'))

        return render_template('index.html', result=result, values=values, error=None)

    except ValueError:
        return render_template('index.html', result=None, values=request.form, error='Please enter valid numeric values for all fields.')
    except Exception as exc:
        return render_template('index.html', result=None, values=request.form, error=str(exc))


def fetch_humidity(latitude, longitude):
    try:
        url = (
            'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}'
            '&hourly=relativehumidity_2m&timezone=auto'
        ).format(latitude=latitude, longitude=longitude)
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.load(response)
        hourly = data.get('hourly', {})
        humidity_values = hourly.get('relativehumidity_2m', [])
        if humidity_values:
            return round(float(humidity_values[0]), 1)
    except Exception:
        pass
    return 65.0


def estimate_soil_values(latitude, longitude):
    nitrogen = 25.0 + abs((latitude % 10) - 5) * 2.0
    phosphorus = 18.0 + abs((longitude % 8) - 4) * 2.5
    potassium = 22.0 + abs(((latitude + longitude) % 12) - 6) * 1.8
    return {
        'nitrogen': round(min(max(nitrogen, 5.0), 60.0), 1),
        'phosphorus': round(min(max(phosphorus, 5.0), 55.0), 1),
        'potassium': round(min(max(potassium, 5.0), 60.0), 1),
    }


@app.route('/location_data', methods=['POST'])
def location_data():
    data = request.get_json(silent=True) or {}
    try:
        latitude = float(data.get('latitude', 0.0))
        longitude = float(data.get('longitude', 0.0))
    except (TypeError, ValueError):
        return jsonify(success=False, error='Invalid location coordinates'), 400

    humidity = fetch_humidity(latitude, longitude)
    soil_values = estimate_soil_values(latitude, longitude)
    return jsonify(
        success=True,
        latitude=latitude,
        longitude=longitude,
        humidity=humidity,
        **soil_values,
    )


if __name__ == '__main__':
    app.run(debug=True)
