from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from opnms.celery import app
from assets.sync.ecssync import AliyunToOpnms
from assets.sync.ecsToopnms import getinit


@shared_task
def ecs_sync():
    data = getinit()

    for instance in data:
        search = {
            'SerialNumber': instance['SerialNumber'],
        }

        a = AliyunToOpnms(search)
        a.main(instance)

