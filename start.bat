@echo off
echo Starting Jugular Vein Detection System...
echo.

echo [1/3] Starting Flask Backend...
start "Backend Server" cmd /k "python app.py"

echo [2/3] Waiting for backend to initialize...
timeout /t 5 /nobreak > nul

echo [3/3] Starting React Frontend...
cd frontend
start "Frontend Server" cmd /k "npm start"

echo.
echo ✅ Both servers are starting up!
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
pause > nul
