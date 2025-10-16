from celery import Celery
from app.config import Config

def make_celery():
    celery = Celery(
        'app',
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND,
        include=['app.tasks']
    )
    return celery

celery = make_celery()
