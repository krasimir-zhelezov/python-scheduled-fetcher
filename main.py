from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime

app = Flask(__name__)

def make_external_request():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        print(f"[{datetime.datetime.now()}] Request made to external site. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error making request: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=make_external_request, trigger="interval", minutes=1)
scheduler.start()

@app.route('/')
def home():
    return "Flask app with scheduled external requests"

if __name__ == '__main__':
    app.run(debug=True)