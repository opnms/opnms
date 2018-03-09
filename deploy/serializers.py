from rest_framework import routers,serializers,viewsets
from .models import SaltGroup,SaltHost,SaltModule
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin,ListBulkCreateUpdateDestroyAPIView,)

class SaltHostSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    '''
    salt host serializer
    '''

    class Meta:
        model = SaltHost
        fields = '__all__'

class SaltGroupSerializer(serializers.ModelSerializer):
    '''
    salt group serializer
    '''

    class Meta:
        model = SaltGroup
        fields = '__all__'

class SaltModuleSerializer(serializers.ModelSerializer):
    '''
    salt module serializer
    '''

    class Meta:
        model = SaltModule
        fields = '__all__'