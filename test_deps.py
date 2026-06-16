#!/usr/bin/env python3
"""Test script to check if dependencies are installed"""

import sys

print("Testing dependencies...")
print(f"Python version: {sys.version}")

try:
    import kivy
    print("✓ Kivy installed:", kivy.__version__)
except ImportError as e:
    print("✗ Kivy NOT installed:", e)

try:
    import numpy
    print("✓ NumPy installed:", numpy.__version__)
except ImportError as e:
    print("✗ NumPy NOT installed:", e)

try:
    import sklearn
    print("✓ scikit-learn installed:", sklearn.__version__)
except ImportError as e:
    print("✗ scikit-learn NOT installed:", e)

try:
    import pandas
    print("✓ pandas installed:", pandas.__version__)
except ImportError as e:
    print("✗ pandas NOT installed:", e)

print("\nTo install missing packages, run:")
print("  pip install -r requirements.txt")
