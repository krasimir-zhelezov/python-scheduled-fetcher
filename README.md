# Scheduled Fetcher
A Flask web application with scheduled background tasks that make periodic external HTTP requests. The app uses APScheduler for job scheduling and includes logging functionality to track request statuses. Environment variables are managed via python-dotenv.

## Features
* Periodic external HTTP requests using APScheduler
* Configurable interval (in minutes) via environment variables
* Comprehensive logging of all requests and errors
* Environment variable configuration with python-dotenv

## Setup
1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-scheduled-requests.git
cd flask-scheduled-requests 
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python main.py
```