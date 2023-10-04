@echo off

echo Installing required Python packages for Web-Sniper...

rem Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 and try again.
    pause
    exit /b 1
)

rem Install the required Python packages using pip
pip install requests
pip install beautifulsoup4
pip install pyfiglet
pip install pytube

rem Check if pip installation was successful
if %errorlevel% neq 0 (
    echo Failed to install required packages. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo Installation completed successfully.
pause
