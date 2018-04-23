from rest_framework import routers,serializers,viewsets
from .models import HttpAlarmPolicy,HttpMonitorGroup,HttpMonitor,HttpEnv
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin,ListBulkCreateUpdateDestroyAPIView,)

__all__ = ['HttpMonitorSerializer','HttpMonitorGroupSerializer','HttpAlarmPolicySerializer','HttpEnvSerializer']

class HttpMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HttpMonitor
        fields = '__all__'

class HttpMonitorGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HttpMonitorGroup
        fields = '__all__'

class HttpAlarmPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = HttpAlarmPolicy
        fields = '__all__'

class HttpEnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = HttpEnv
        fields = '__all__'