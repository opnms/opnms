from rest_framework import routers,serializers,viewsets
from .models import SaltGroup,SaltHost
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin,ListBulkCreateUpdateDestroyAPIView,)

class SaltHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltHost
        fields = '__all__'
class SaltGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltGroup
        fields = '__all__'