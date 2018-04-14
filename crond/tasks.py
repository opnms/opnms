import time
from crond import celery_app
from datetime import timedelta
from celery.schedules import crontab,schedule
from celery import shared_task,task

@shared_task
def add(x, y):
    time.sleep(2)
    return x + y

@shared_task
def multiply(x, y):
    time.sleep(2)
    return x * y
