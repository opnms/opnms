from rest_framework import routers,viewsets
from ..models import Cloudprovider
from rest_framework_bulk import BulkModelViewSet

from ..serializers import CloudProviderSerializer

class CloudProviderViewSet(viewsets.ModelViewSet):
    queryset = Cloudprovider.objects.all()
    serializer_class = CloudProviderSerializer