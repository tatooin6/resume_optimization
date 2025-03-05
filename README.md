![Linting](https://github.com/tatooin6/resume_optimization/actions/workflows/linting.yml/badge.svg)

# Resume Optimizer with Google Gemini and FastAPI

This project allows to optimize resumes based on a job description using the Google Gemini API.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tatooin6/resume_optimization.git resumer
cd resumer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

Or you can install them manually (this may change in the future):
```txt
fastapi
uvicorn
google-generativeai
markdown
weasyprint
python-dotenv
pytest
flake8
celery
redis
```

4. Create an .env file and add your Google Gemini API Key:
```bash
GEMINI_API_KEY="api-key-here"
```

## Usage
1. Upload a resume in Markdown format.
2. Enter the job description.
3. Download the optimized resume in PDF format. (When fastAPI is integrated to the service)

## Technologies Used
- Python + FastAPI (future implementation)
- Google Gemini API
- Markdown + WeasyPrint (for PDF conversion)
- Uvicorn (to run the server)(future implementation)

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

#### Formating
To check formating run the next command:
```bash
flake8 app/ tests/
```


