from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from .. import api

# router = routers.DefaultRouter()
router = BulkRouter()
router.register(r'v1/instance',api.InstanceViewSet,'instance')
router.register(r'v1/region',api.RegionViewSet,'region')
router.register(r'v1/cloud',api.CloudProviderViewSet,'cloud')
router.register(r'v1/server',api.ServerViewSet,'server')
app_name = 'assets'

urlpatterns = [
    # url(r'^v1/instance-bulk/$',api.InstanceUpdateAPI.as_view(),'instance-bulk-update'),
]
urlpatterns += router.urls