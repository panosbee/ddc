@echo off
SETLOCAL EnableDelayedExpansion

ECHO ================================================================
ECHO Diabetes Management Platform - Installation Script
ECHO ================================================================
ECHO.
ECHO This script will install all dependencies and create the admin user.
ECHO Please ensure MongoDB is installed and running before proceeding.
ECHO.

REM --- Check Prerequisites ---
ECHO Checking prerequisites...

REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    ECHO ✗ Python is not installed or not in PATH
    ECHO Please install Python 3.8+ and try again
    PAUSE
    EXIT /B 1
)
ECHO ✓ Python found

REM Check if Node.js is installed
node --version >nul 2>&1
IF ERRORLEVEL 1 (
    ECHO ✗ Node.js is not installed or not in PATH
    ECHO Please install Node.js 16+ and try again
    PAUSE
    EXIT /B 1
)
ECHO ✓ Node.js found

REM Check if .env file exists
IF NOT EXIST .env (
    ECHO ✗ .env file not found
    ECHO Please copy .env.template to .env and configure it with your API keys
    ECHO Then run this script again
    PAUSE
    EXIT /B 1
)
ECHO ✓ .env file found

ECHO.
ECHO Prerequisites check passed. Starting installation...
ECHO.

REM --- Backend Setup ---
ECHO [1/4] Setting up Python virtual environment...
IF NOT EXIST diabetes_backend\venv (
    python -m venv diabetes_backend\venv
    IF ERRORLEVEL 1 (
        ECHO ✗ Failed to create virtual environment
        PAUSE
        EXIT /B 1
    )
)
ECHO ✓ Virtual environment ready

ECHO [2/4] Installing Python dependencies...
call diabetes_backend\venv\Scripts\activate.bat && pip install -r diabetes_backend\requirements.txt && deactivate
IF ERRORLEVEL 1 (
    ECHO ✗ Failed to install Python dependencies
    PAUSE
    EXIT /B 1
)
ECHO ✓ Python dependencies installed

REM --- Frontend Setup ---
ECHO [3/4] Installing Doctor Portal packages...
cd /D diabetes_frontend
call npm install
IF ERRORLEVEL 1 (
    ECHO ✗ Failed to install Doctor Portal dependencies
    cd ..
    PAUSE
    EXIT /B 1
)
cd ..
ECHO ✓ Doctor Portal dependencies installed

ECHO Installing Patient PWA packages...
cd /D diabetes_patient_pwa
call npm install
IF ERRORLEVEL 1 (
    ECHO ✗ Failed to install Patient PWA dependencies
    cd ..
    PAUSE
    EXIT /B 1
)
cd ..
ECHO ✓ Patient PWA dependencies installed

REM --- Admin User Creation ---
ECHO [4/4] Creating admin user...
cd diabetes_backend
call venv\Scripts\activate.bat && python create_admin_user.py && deactivate
IF ERRORLEVEL 1 (
    ECHO ✗ Failed to create admin user
    ECHO Please check that MongoDB is running and try again
    cd ..
    PAUSE
    EXIT /B 1
)
cd ..
ECHO ✓ Admin user created

ECHO.
ECHO ================================================================
ECHO Installation completed successfully!
ECHO ================================================================
ECHO.
ECHO Next steps:
ECHO 1. Run: run.bat
ECHO 2. Open http://localhost:5173 in your browser
ECHO 3. Login with username: admin, password: admin123
ECHO 4. Change the default password immediately!
ECHO.
ECHO ⚠ IMPORTANT: Change the admin password after first login!
ECHO.
PAUSE
