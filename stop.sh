echo "Stopping services..."

pkill -f redis-server
pkill -f uvicorn
pkill -f celery

echo "Services stopped..."

