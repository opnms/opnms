from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from .. import api

# router = routers.DefaultRouter()
router = BulkRouter()
router.register(r'v1/service',api.ServiceViewSet,'service')

app_name = 'business'

urlpatterns = []
urlpatterns += router.urls