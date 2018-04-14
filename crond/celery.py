from __future__ import absolute_import
import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opnms.settings')
app = Celery('opnms')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks(lambda: [app_config.split('.')[0] for app_config in settings.INSTALLED_APPS])



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


