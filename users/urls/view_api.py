from django.conf.urls import url,include
from rest_framework import routers
from .. import api
from rest_framework_bulk.routes import BulkRouter


app_name = 'users'
# router = routers.DefaultRouter()
router = BulkRouter()
router.register(r'v1/users',api.UserViewSet,'user')
router.register(r'v1/groups',api.GroupViewSet,'group')
router.register(r'v1/department',api.DepartmentViewSet,'department')
router.register(r'v1/saltapi',api.SaltApiView,'saltapi')

urlpatterns = []
urlpatterns += router.urls