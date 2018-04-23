from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from .. import api

# router = routers.DefaultRouter()
router = BulkRouter()
router.register(r'v1/httpmonitor',api.HttpMonitorViewSet,'http')
router.register(r'v1/httpgroup',api.HttpMonitorGroupViewSet,'http-group')
router.register(r'v1/httpalarmpolicy',api.HttpAlarmPolicyViewSet,'http-alarmpolicy')
router.register(r'v1/httpenv',api.HttpEnvViewSet,'http-env')


app_name = 'monitor'

urlpatterns = []
urlpatterns += router.urls