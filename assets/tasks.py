from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from opnms.celery import app
from assets.sync.ecssync import AliyunToOpnms
from assets.sync.ecsToopnms import getinit
from deploy.saltstack.saltapi import SaltstackAPI
import json
import requests
from base.apis import salthost_create_or_update

@shared_task
def ecs_sync():
    data = getinit()

    for instance in data:
        search = {
            'SerialNumber': instance['SerialNumber'],
        }

        a = AliyunToOpnms(search)
        a.main(instance)

@shared_task
def salt_host_create_update():
    minion_info = SaltstackAPI()
    print(minion_info.list_all_key())
    url = 'http://127.0.0.1:8000/api/deploys/v1/salthost/'

    for minion in minion_info.list_all_key():

        search = {
            'minion': minion,
        }

        api = salthost_create_or_update(url=url,search=search)
        api.main({'minion':minion})
