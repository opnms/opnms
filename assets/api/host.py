from rest_framework import routers,viewsets
from ..models import Host
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import HostSerializer


__all__ = ['HostViewSet',]


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def get_queryset(self):
        queryset = super(HostViewSet,self).get_queryset()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset