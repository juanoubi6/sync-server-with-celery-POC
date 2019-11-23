from datetime import datetime

from celery import group
from flask import Flask

from celery_app.tasks import execute_http_call

app = Flask(__name__)


@app.route('/io-bound-task')
def io_bound_task():
    start = datetime.now()

    five_secs_endpoint = 'https://postman-echo.com/delay/5'
    three_secs_endpoint = 'https://postman-echo.com/delay/3'
    one_sec_endpoint = 'https://postman-echo.com/delay/1'

    # This tasks are executed:
    # - In parallel: if celery is using workers (and we have enough workers)
    # - Concurrently: if we use thread pools with eventlet
    task_group = group([
        execute_http_call.si(five_secs_endpoint),
        execute_http_call.si(three_secs_endpoint),
        execute_http_call.si(one_sec_endpoint)
    ])()
    results = task_group.get()

    end = datetime.now()

    final_time = end - start

    return {"results": results, "time": final_time.total_seconds()}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001, debug=True)
