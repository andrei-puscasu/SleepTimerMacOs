#!/bin/bash
# Quick Start Script for Sleep Timer Menu Bar App

echo "🚀 Sleep Timer Setup"
echo "===================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Dependencies installed successfully!"
    echo ""
    echo "Choose an option:"
    echo "  1) Run the app now (test mode)"
    echo "  2) Build standalone app bundle"
    read -p "Enter choice (1 or 2): " choice
    
    case $choice in
        1)
            echo ""
            echo "🚀 Starting Sleep Timer..."
            python3 sleep_timer_menubar.py
            ;;
        2)
            echo ""
            echo "🔨 Building standalone app..."
            python3 setup.py py2app
            
            if [ $? -eq 0 ]; then
                echo ""
                echo "✅ App built successfully!"
                echo "📁 Location: dist/SleepTimer.app"
                echo ""
                echo "Next steps:"
                echo "  1. Open Finder and navigate to the 'dist' folder"
                echo "  2. Drag SleepTimer.app to your Applications folder"
                echo "  3. Double-click to launch!"
            else
                echo "❌ Build failed. Please check error messages above."
            fi
            ;;
        *)
            echo "Invalid choice. Run this script again."
            exit 1
            ;;
    esac
else
    echo "❌ Failed to install dependencies."
    echo "Please check your internet connection and try again."
    exit 1
fi
