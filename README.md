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

