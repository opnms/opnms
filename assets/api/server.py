from rest_framework import routers,viewsets
from ..models import Server
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import ServerSerializer


__all__ = ['ServerViewSet',]


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    # permission_classes =
    # lookup_field =

    def get_queryset(self):
        queryset = super(ServerViewSet,self).get_queryset()
        serialnumber = self.request.query_params.get('serialnumber',None)
        if serialnumber is not None:
            queryset = queryset.filter(serialnumber=serialnumber)
        return queryset