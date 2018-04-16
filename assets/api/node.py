from rest_framework import routers,viewsets
from ..models import Node
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import NodeSerializer


__all__ = ['NodeViewSet',]


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def get_queryset(self):
        queryset = super(NodeViewSet,self).get_queryset()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset