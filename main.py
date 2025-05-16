from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime
import os
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)

logging.basicConfig(
    filename='.log',
    filemode='a', 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def make_external_request():
    try:
        response = requests.get(os.environ.get('URL'))
        logging.info(f'Request made to external site. Status code: {response.status_code}')
    except Exception as e:
        logging.error(f'Error while making request: {e}')

scheduler = BackgroundScheduler()
scheduler.add_job(func=make_external_request, trigger="interval", minutes=int(os.environ.get('INTERVAL_IN_MINUTES')))
scheduler.start()

@app.route('/')
def home():
    return "Flask app with scheduled external requests"

if __name__ == '__main__':
    app.run(debug=True)