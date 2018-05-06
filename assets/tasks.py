from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from base.base import OpnmsCreateUpdate
from .sync.ecsToopnms import getinit
from deploy.saltstack.saltapi import SaltstackAPI
from assets.models import Cloudprovider,Region
from base.apis import salthost_create_or_update
from base.ews_service import  EwsService
# cloud = Cloudprovider.objects.all()
# print(cloud)


@shared_task
def ecs_sync():
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/instance/'
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

            a = OpnmsCreateUpdate(url=opnms_url,search=search)
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


@shared_task
def container_create_or_update():
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/container/'

    ews = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939'
        )
    containers = ews.get(geturl='http://open-ews.cloud.tmall.com/api/v1/container')

    print(containers)
    if containers['code'] == '0':
        for container in containers['data']:
            search = {
                'id': container['id'],
            }
            serviceAction = OpnmsCreateUpdate(url=opnms_url,search=search)
            serviceAction.main(container)

@shared_task
def image_create_or_update():
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/image/'

    ews = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939'
    )
    images = ews.ews.get(geturl='http://open-ews.cloud.tmall.com/api/v1/image')

    # print(images)
    if images['code'] == '0':
        for image in images['data']:
            search = {
                'id': image['id'],
            }
            imageAction = OpnmsCreateUpdate(url=opnms_url,search=search)
            imageAction.main(image)


@shared_task
def Host_create_or_update():
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/host/'

    ews = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939',
    )
    hosts = ews.get(geturl='http://open-ews.cloud.tmall.com/api/v1/host')

    # print(images)
    if hosts['code'] == '0':
        for host in hosts['data']:
            search = {
                'id': host['id'],
            }
            hostAction = OpnmsCreateUpdate(url=opnms_url, search=search)
            hostAction.main(host)


@shared_task
def Node_create_or_update():
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/node/'

    ews = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939'
    )
    nodes = ews.get(geturl='http://open-ews.cloud.tmall.com/api/v1/node')

    # print(images)
    if nodes['code'] == '0':
        for node in nodes['data']:
            search = {
                'id': node['id'],
            }
            nodeAction = OpnmsCreateUpdate(url=opnms_url, search=search)
            nodeAction.main(node)