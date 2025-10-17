#!/bin/bash

echo "Starting Jugular Vein Detection System..."
echo

echo "[1/3] Starting Flask Backend..."
python app.py &
BACKEND_PID=$!

echo "[2/3] Waiting for backend to initialize..."
sleep 5

echo "[3/3] Starting React Frontend..."
cd frontend
npm start &
FRONTEND_PID=$!

echo
echo "✅ Both servers are starting up!"
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:3000"
echo
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo "Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit
}

# Trap Ctrl+C
trap cleanup SIGINT

# Wait for both processes
wait
