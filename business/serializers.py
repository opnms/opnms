from rest_framework import routers,serializers,viewsets
from .models import Project,Service
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin,ListBulkCreateUpdateDestroyAPIView,)

__all__ = ['ServiceSerializer']

class ServiceSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    # VpcAttributes = serializers.ListField()
    nodes = serializers.ListField()
    class Meta:
        model = Service
        fields = '__all__'