@echo off
title GeekVerse Launcher

echo ===============================
echo      INICIANDO GEEKVERSE
echo ===============================
echo.

start cmd /k "cd Backend && .venv\Scripts\Activate && python -m uvicorn main:app --reload"

timeout /t 3 >nul

start cmd /k "cd Frontend && python -m http.server 5500"

timeout /t 2 >nul

start http://127.0.0.1:5500

exit