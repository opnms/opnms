from rest_framework import routers,viewsets
from ..models import Image
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import ImageSerializer


__all__ = ['ImageViewSet',]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = super(ImageViewSet,self).get_queryset()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset