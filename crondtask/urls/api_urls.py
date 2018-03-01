from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from .. import api

app_name = 'crondtask'

router = BulkRouter()
router.register(r'v1/crontab',api.CrontabViewSet,'crontab')
router.register(r'v1/interval',api.IntervalViewSet,'interval')
router.register(r'v1/periodic',api.PeriodicTasksViewSet,'periodic')
# router.register(r'v1/solar',api.SolarScheduleViewSet,'solar')


urlpatterns = [
    # url(r'^v1/instance-bulk/$',api.InstanceUpdateAPI.as_view(),'instance-bulk-update'),
]
urlpatterns += router.urls