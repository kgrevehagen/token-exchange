#!/bin/bash

echo "Creating a virtual environment..."
python -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Installing dependencies for local development..."
pip install -r requirements.txt

echo "Installing dependencies for packaging..."
pip install -r requirements.txt -t package/

echo "Setup complete."