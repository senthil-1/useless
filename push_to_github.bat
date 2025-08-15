@echo off
echo 🐙 FridgeMood.AI - GitHub Push Script
echo ====================================

echo.
echo 📋 Files to be pushed:
echo ✅ index12.html (Main frontend)
echo ✅ app_final_random.py (Local server)
echo ✅ api/app.py (Vercel backend)
echo ✅ vercel.json (Deployment config)
echo ✅ requirements.txt (Dependencies)
echo ✅ README.md (Project documentation)
echo ✅ DEPLOYMENT_GUIDE.md (Deployment guide)

echo.
echo 🔧 Git operations:

echo Adding all files...
git add .

echo.
set /p commit_message="Enter commit message (or press Enter for default): "
if "%commit_message%"=="" set commit_message=Add FridgeMood.AI - Random mood generator for fridge contents

echo Committing with message: "%commit_message%"
git commit -m "%commit_message%"

echo.
echo 🚀 Pushing to GitHub...
git push

echo.
echo 🎉 Push complete!
echo.
echo 📋 Next steps:
echo 1. Check your GitHub repository
echo 2. Deploy to Vercel using the repo
echo 3. Share your live app URL!
echo.
pause
