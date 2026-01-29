@echo off
REM Password Cracking Dashboard - Quick Start Script
REM Windows Batch File

echo.
echo =====================================================
echo  Password Cracking Dashboard - Quick Start
echo =====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version

echo.
echo [2/4] Installing dependencies...
pip install -r requirements.txt

echo.
echo [3/4] Initializing database...
python -c "from database import init_db; init_db(); print('Database initialized successfully')"

echo.
echo [4/4] Starting Flask application...
echo.
echo =====================================================
echo  Server running at: http://127.0.0.1:5000
echo.
echo  Demo Credentials:
echo    Username: demo
echo    Password: DemoPassword123!
echo.
echo  Press Ctrl+C to stop the server
echo =====================================================
echo.

python app.py

pause
