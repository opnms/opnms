from rest_framework import routers,viewsets
from ..models import Instance
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import InstanceSerializer


__all__ = ['InstanceViewSet',]


class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    # permission_classes =
    # lookup_field =

    def get_queryset(self):
        queryset = super(InstanceViewSet,self).get_queryset()
        SerialNumber = self.request.query_params.get('SerialNumber',None)
        if SerialNumber is not None:
            queryset = queryset.filter(SerialNumber=SerialNumber)
        return queryset

    # permission_classes =

