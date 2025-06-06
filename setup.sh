#!/bin/bash

# BSI AI Extractor Setup Script
echo "Setting up BSI AI Extractor..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

echo "Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup complete! To use the BSI AI Extractor:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the script: python script.py"
echo ""
echo "Make sure you have the 'AI-Finance_Test-Criteria.pdf' file in this directory."
