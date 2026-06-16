#!/usr/bin/env python3
"""
Crop Recommendation System - Kivy Mobile App Entry Point
"""

from kivy.app import App
from kivy.core.window import Window
from src.models.crop_model import CropRecommendationModel
from src.ui.screens import CropRecommenderScreen

# Set window size for desktop testing; ignored on mobile.
Window.size = (360, 640)


class CropRecommenderApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = CropRecommendationModel()
        self.screen = CropRecommenderScreen(self.model)

    def build(self):
        self.title = 'Crop Recommendation'
        return self.screen.create_main_layout()


if __name__ == '__main__':
    CropRecommenderApp().run()
