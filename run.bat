@echo off
REM MathPix LaTeX Extractor - Setup and Run Script (Windows)
REM This script automatically sets up the environment and runs the application

echo 🚀 MathPix LaTeX Extractor Setup ^& Run Script
echo ==============================================

REM Get the directory where this script is located
cd /d "%~dp0"

echo 📁 Working directory: %CD%

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo    Please install Python and try again
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo 📈 Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
if exist "requirements.txt" (
    pip install -r requirements.txt
) else (
    echo 📝 Installing core dependencies...
    pip install flask requests python-dotenv
)

echo ✅ Dependencies installed

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  Warning: .env file not found!
    echo    Creating .env from template...
    
    if exist ".env.example" (
        copy ".env.example" ".env"
        echo 📝 Created .env file from template
        echo ⚠️  IMPORTANT: Please edit .env and add your MathPix API credentials:
        echo    - MATHPIX_APP_ID=your_app_id_here
        echo    - MATHPIX_APP_KEY=your_app_key_here
        echo.
        echo Press Enter to continue after editing .env...
        pause >nul
    ) else (
        echo ❌ Error: No .env.example file found
        echo    Please create a .env file with your MathPix API credentials
        pause
        exit /b 1
    )
) else (
    echo ✅ .env file found
)

REM Verify environment variables
echo 🔍 Checking environment variables...
python -c "import os; from dotenv import load_dotenv; load_dotenv(); app_id = os.getenv('MATHPIX_APP_ID'); app_key = os.getenv('MATHPIX_APP_KEY'); exit(1) if not app_id or not app_key else print(f'✅ API credentials found (ID: {app_id[:10]}...)')"

if errorlevel 1 (
    echo ❌ Environment variable check failed
    echo    Please check your MATHPIX_APP_ID and MATHPIX_APP_KEY in .env
    pause
    exit /b 1
)

REM Check if app.py exists
if not exist "app.py" (
    echo ❌ Error: app.py not found
    echo    Make sure you're running this script from the project directory
    pause
    exit /b 1
)

echo ✅ Application file found

echo.
echo 🎉 Setup complete! Starting the application...
echo 📱 The app will be available at: http://127.0.0.1:5000
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Run the application
python app.py
