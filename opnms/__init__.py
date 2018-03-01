from __future__ import absolute_import

# from .crontab import app as celery_app
from .celery import app as celery_app

__all__ = ['celery_app']