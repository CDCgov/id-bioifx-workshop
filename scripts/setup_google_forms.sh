#!/bin/bash
#
# Quick setup script for Google Forms automation
#
# This script helps you set up the Python environment and dependencies
# needed to run the Google Forms creation script.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "===================================="
echo "Google Forms Setup Script"
echo "===================================="
echo ""

# Check Python version
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher first"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install/upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo "✅ pip upgraded"
echo ""

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt --quiet
echo "✅ Python packages installed"
echo ""

# Check for credentials
echo "Checking for Google API credentials..."
if [ ! -f "credentials.json" ]; then
    echo "⚠️  Warning: credentials.json not found"
    echo ""
    echo "To complete setup, you need to:"
    echo "1. Go to https://console.cloud.google.com/"
    echo "2. Create/select a project"
    echo "3. Enable Google Forms API"
    echo "4. Create OAuth 2.0 credentials (Desktop app)"
    echo "5. Download credentials.json to this directory"
    echo ""
    echo "See README_GOOGLE_FORMS.md for detailed instructions"
    echo ""
    exit 1
else
    echo "✅ credentials.json found"
fi
echo ""

# All set!
echo "===================================="
echo "✅ Setup complete!"
echo "===================================="
echo ""
echo "To create a Google Form, run:"
echo "  source venv/bin/activate"
echo "  python create_google_form.py"
echo ""
echo "Or simply:"
echo "  ./venv/bin/python create_google_form.py"
echo ""
echo "For help:"
echo "  python create_google_form.py --help"
echo ""
