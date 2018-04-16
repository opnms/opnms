from rest_framework import routers,viewsets
from ..models import Container
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import ContainerSerializer


__all__ = ['ContainerViewSet',]


class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

    def get_queryset(self):
        queryset = super(ContainerViewSet,self).get_queryset()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset