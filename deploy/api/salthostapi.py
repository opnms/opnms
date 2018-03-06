from rest_framework import routers,viewsets
from ..models import SaltGroup,SaltHost
from ..serializers import SaltHostSerializer,SaltGroupSerializer


__all__ = ['SaltHostViewSet','SaltGroupViewSet']

class SaltHostViewSet(viewsets.ModelViewSet):
    queryset = SaltHost.objects.all()
    serializer_class = SaltHostSerializer


class SaltGroupViewSet(viewsets.ModelViewSet):
    queryset = SaltGroup.objects.all()
    serializer_class = SaltGroupSerializer