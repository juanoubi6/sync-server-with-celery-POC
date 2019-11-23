import requests

from .celery import app


@app.task
def execute_http_call(url):
    response = requests.get(url)
    return response.status_code



