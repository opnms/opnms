from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from opnms.celery import app
from .sync.ecssync import AliyunToOpnms
from .sync.ecsToopnms import getinit
from deploy.saltstack.saltapi import SaltstackAPI
from assets.models import Cloudprovider,Region
import json
import requests
from base.apis import salthost_create_or_update

# cloud = Cloudprovider.objects.all()
# print(cloud)

@shared_task
def ecs_sync():
    cloud = Cloudprovider.objects.all()
    for mes in cloud:
        id = mes.id
        key = mes.keyid
        serect = mes.keysecret
        region_info = Region.objects.get(provider=id)

        data = getinit(key,serect,region_info.name)

        for instance in data:
            search = {
                'SerialNumber': instance['SerialNumber'],
            }

            a = AliyunToOpnms(search)
            a.main(instance)

@shared_task
def salt_host_create_update():
    minion_info = SaltstackAPI()
    url = 'http://127.0.0.1:8000/api/deploys/v1/salthost/'

    for minion in minion_info.list_all_key():

        search = {
            'minion': minion,
        }

        api = salthost_create_or_update(url=url,search=search)
        api.main({'minion':minion})
