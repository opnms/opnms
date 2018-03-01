from rest_framework import routers,serializers,viewsets
from .models import Instance,Region,Cloudprovider,Server
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin,ListBulkCreateUpdateDestroyAPIView,)

class InstanceSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    # VpcAttributes = serializers.ListField()
    InnerIpAddress = serializers.ListField()
    PublicIpAddress = serializers.ListField()
    SecurityGroupIds = serializers.ListField()
    EipAddress = serializers.ListField()
    VpcAttributes = serializers.ListField()
    OperationLocks = serializers.ListField()
    class Meta:
        model = Instance
        fields = '__all__'



class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CloudProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloudprovider
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'