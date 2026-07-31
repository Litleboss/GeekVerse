@echo off
title GeekVerse Launcher

cd /d "%~dp0"

echo ===============================
echo       INICIANDO GEEKVERSE
echo ===============================
echo.

echo Iniciando Backend...
start "GeekVerse Backend" cmd /k "cd /d "%~dp0Backend" && ".venv\Scripts\python.exe" -m uvicorn main:app --reload"

timeout /t 3 /nobreak >nul

echo Iniciando Frontend...
start "GeekVerse Frontend" cmd /k "cd /d "%~dp0Frontend" && python -m http.server 5500"

timeout /t 3 /nobreak >nul

echo Abrindo o navegador...
start "" "http://127.0.0.1:5500"

exit