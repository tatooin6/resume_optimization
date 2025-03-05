#!/bin/bash

echo "Starting Services..."

# REDIS
echo "Iniciando Reddis"
redis-server &
REDIS_PID=$!
sleep 2

if ps -p $REDIS_PID > /dev/null; then
    echo "OK - Redis initialized correctly"
else
    echo "ERROR - Redis has not been initialized correctly. Aborting script."
    exit 1
fi

# FASTAPI
echo "Initializing FastAPI server"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
UVICORN_PID=$!
sleep 2

if ps -p $UVICORN_PID > /dev/null; then
    echo "OK - FastAPI initialized successfully"
else
    echo "ERROR - FastAPI was not initialized correctly. Aborting script."
    exit 1
fi

# Celery
echo "Starting Celery Worker"
celery -A app.celery_config worker --loglevel=info --queues=resume_task &
CELERY_PID=$!
sleep 2

if ps -p $CELERY_PID > /dev/null; then
    echo "OK - Celery initialized successfully"
else
    echo "ERROR - Celery has not initialized correctly. Aborting script."
    exit 1
fi

echo "All services started successfully."
wait
