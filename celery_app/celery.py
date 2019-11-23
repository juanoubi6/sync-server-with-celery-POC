from celery import Celery

app = Celery(
    'celery_tasks',
    broker='redis://redis:6379/1',
    backend='redis://redis:6379/1',
    include=['celery_app.tasks']
)

if __name__ == '__main__':
    app.start()
