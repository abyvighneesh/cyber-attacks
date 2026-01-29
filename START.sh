#!/bin/bash
# Password Cracking Dashboard - Quick Start Script
# Linux/macOS

echo ""
echo "====================================================="
echo "  Password Cracking Dashboard - Quick Start"
echo "====================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from python.org"
    exit 1
fi

echo "[1/4] Checking Python installation..."
python3 --version

echo ""
echo "[2/4] Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "[3/4] Initializing database..."
python3 -c "from database import init_db; init_db(); print('Database initialized successfully')"

echo ""
echo "[4/4] Starting Flask application..."
echo ""
echo "====================================================="
echo "  Server running at: http://127.0.0.1:5000"
echo ""
echo "  Demo Credentials:"
echo "    Username: demo"
echo "    Password: DemoPassword123!"
echo ""
echo "  Press Ctrl+C to stop the server"
echo "====================================================="
echo ""

python3 app.py
