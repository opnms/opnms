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
    minions = serializers.SlugRelatedField(many=True,read_only=True,slug_field='minion')
    class Meta:
        model = SaltGroup
        fields = ('id','name','abbr_name','minions','comment',)

class SaltModuleSerializer(serializers.ModelSerializer):
    '''
    salt module serializer
    '''

    class Meta:
        model = SaltModule
        fields = '__all__'