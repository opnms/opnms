from rest_framework import routers,viewsets
from ..models import Region
from ..serializers import RegionSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
