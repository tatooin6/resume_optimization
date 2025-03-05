## For Developers

### Redis
Installing on Mac with
```bash
brew install redis
```

To execute redis server enter
```bash
redis-server
```
--- 
Installing on Linux with
```bash
sudo apt install redis -y
```

And start it with
```bash
sudo systemctl start redis
```
---
Installing on Windows with
```bash
docker run -d --name redis -p 6379:6379 redis
```
---
On any of the previous os test if Redis is working with
```bash
redis-cli ping
``` 
It should response with "PONG", that means all's good

#### Usage

To start Redis:
```bash
redis-server
```

Start Uvicorn server:
```bash
uvicorn app.main:app --reload
```
If there are problems with this then we start the server providing more data:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Start Celery:
```bash
celery -A app.celery_config.celery_app worker --loglevel=info
```
or
```bash
celery -A app.celery_config worker --loglevel=info --queues=resume_task
```

To start all the services you can run start.sh on the terminal. If all the services start succesfully 
A message "All services started successfully." would be displayed on the screen.
All the processes can be listed with:
```bash
ps aux | grep redis
ps aux | grep uvicorn
ps aux | grep celery
```

It is possible to stop processes one by one with:
```bash
kill -9 12345   # Redis
kill -9 67890   # Uvicorn
kill -9 45678   # Celery
```

Otherwise, there is an option to do this faster with:
```bash
pkill -f redis-server
pkill -f uvicorn
pkill -f celery
```

In order to stop all the services at once run stop.sh. 

It is possible to track all the services on independent windows, once tmux is intialized:
```bash
tmux new-session -d -s resume_optimization
tmux split-window -h
tmux split-window -v
```

To execute each service on different window:
```bash
tmux send-keys -t 0 "redis-server" C-m
tmux send-keys -t 1 "uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload" C-m
tmux send-keys -t 2 "celery -A app.celery_config worker --loglevel=info" C-m
```

To join the session and look at the logs on real time:
```bash
tmux attach -t resume_optimization
```
