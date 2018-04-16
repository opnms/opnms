from __future__ import absolute_import, unicode_literals
import time
from crond import celery_app
from datetime import timedelta
from celery.schedules import crontab,schedule
from celery import shared_task,task
from base.base import OpnmsCreateUpdate
from base.ews_service import EwsService

class ServiceCreateUpdate(OpnmsCreateUpdate):
    pass


@shared_task
def services_create_or_update():
    opnms_url = 'http://127.0.0.1:8000/api/business/v1/service/'

    ews = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939',
        url='http://open-ews.cloud.tmall.com/api/v1/service/'
        )
    services = ews.EwsSign()

    # print(services)
    if services['code'] == '0':
        for service in services['data']:
            search = {
                'id': service['id'],
            }
            serviceAction = OpnmsCreateUpdate(url=opnms_url,search=search)
            serviceAction.main(service)




