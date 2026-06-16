#!/usr/bin/env python3
"""
Crop Recommendation System - Command Line Version
AI-powered crop recommendation without GUI
"""

from src.models.crop_model import CropRecommendationModel


def get_user_input():
    """Get soil parameters from user"""
    print("\n🌱 Crop Recommendation System")
    print("=" * 40)

    try:
        nitrogen = float(input("Nitrogen (kg/hectare, 0-100): "))
        phosphorus = float(input("Phosphorus (kg/hectare, 0-100): "))
        potassium = float(input("Potassium (kg/hectare, 0-100): "))
        temperature = float(input("Temperature (°C, 10-50): "))
        humidity = float(input("Humidity (%, 0-100): "))
        ph = float(input("Soil pH (3-9): "))
        rainfall = float(input("Rainfall (mm, 0-300): "))

        return nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return None


def main():
    """Main application"""
    print("Loading ML model...")
    model = CropRecommendationModel()

    while True:
        params = get_user_input()
        if params is None:
            continue

        print("\n🔍 Analyzing soil conditions...")
        result = model.predict(*params)

        if result['success']:
            print("\n✅ Recommendation Results:")
            print(f"🏆 Primary Crop: {result['primary_crop']}")

            print("\n📊 Top Recommendations:")
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"{i}. {rec['crop']} ({rec['confidence']:.1f}%)")

            print("\n💡 Tip: These recommendations are based on your soil parameters.")
            print("   Actual results may vary based on local conditions.")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")

        try:
            again = input("\n🔄 Analyze another set of data? (y/n): ").lower().strip()
            if again not in ['y', 'yes']:
                break
        except KeyboardInterrupt:
            break

    print("\n👋 Thank you for using Crop Recommendation System!")


if __name__ == '__main__':
    main()
