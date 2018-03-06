from django.conf.urls import url,include
from rest_framework_bulk.routes import BulkRouter
from .. import api

router = BulkRouter()
router.register(r'v1/salthost',api.SaltHostViewSet,'salthost')
router.register(r'v1/saltgroup',api.SaltGroupViewSet,'saltgroup')

app_name = 'deploy'

urlpatterns = [
    # url(r'^v1/instance-bulk/$',api.InstanceUpdateAPI.as_view(),'instance-bulk-update'),
]
urlpatterns += router.urls