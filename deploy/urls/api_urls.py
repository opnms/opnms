from django.conf.urls import url,include
from rest_framework_bulk.routes import BulkRouter
from .. import api

router = BulkRouter()
router.register(r'v1/salthost',api.SaltHostViewSet,'salthost')
router.register(r'v1/saltgroup',api.SaltGroupViewSet,'saltgroup')
router.register(r'v1/saltmodule',api.SaltModuleViewset,'saltmodule')

app_name = 'deploy'

urlpatterns = [
    url(r'v1/salthost/(?P<pk>\d+)/detail/$',api.SaltHostListApi.as_view(),name='salthost-detail'),
]
urlpatterns += router.urls