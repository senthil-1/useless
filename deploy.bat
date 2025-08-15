@echo off
echo 🚀 FridgeMood.AI - Vercel Deployment Script
echo ============================================

echo.
echo 📋 Checking required files...

if not exist "index12.html" (
    echo ❌ index12.html not found!
    pause
    exit /b 1
)

if not exist "api\app.py" (
    echo ❌ api\app.py not found!
    pause
    exit /b 1
)

if not exist "vercel.json" (
    echo ❌ vercel.json not found!
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ❌ requirements.txt not found!
    pause
    exit /b 1
)

echo ✅ All required files found!

echo.
echo 🔧 Installing Vercel CLI (if not installed)...
npm list -g vercel >nul 2>&1
if errorlevel 1 (
    echo Installing Vercel CLI...
    npm install -g vercel
) else (
    echo ✅ Vercel CLI already installed
)

echo.
echo 🚀 Deploying to Vercel...
echo.
echo Follow these steps:
echo 1. Login to Vercel when prompted
echo 2. Choose project name (e.g., fridgemood-ai)
echo 3. Select "Other" as framework
echo 4. Leave build command empty
echo 5. Leave output directory empty
echo.

vercel

echo.
echo 🎉 Deployment complete!
echo Your app should be live at the URL shown above.
echo.
pause
