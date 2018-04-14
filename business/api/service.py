from rest_framework import routers,viewsets
from ..models import Service
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import ServiceSerializer


__all__ = ['ServiceViewSet',]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


    def get_queryset(self):
        queryset = super(ServiceViewSet,self).get_queryset()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset