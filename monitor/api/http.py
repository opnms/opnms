from rest_framework import routers,viewsets
from ..models import HttpMonitor,HttpEnv,HttpMonitorGroup,HttpAlarmPolicy
from rest_framework import generics
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from ..serializers import HttpAlarmPolicySerializer,HttpEnvSerializer,HttpMonitorGroupSerializer,HttpMonitorSerializer


__all__ = ['HttpMonitorViewSet','HttpMonitorGroupViewSet','HttpAlarmPolicyViewSet','HttpEnvViewSet']


class HttpMonitorViewSet(viewsets.ModelViewSet):
    queryset = HttpMonitor.objects.all()
    serializer_class = HttpMonitorSerializer


class HttpMonitorGroupViewSet(viewsets.ModelViewSet):
    queryset = HttpMonitorGroup.objects.all()
    serializer_class = HttpMonitorGroupSerializer


class HttpAlarmPolicyViewSet(viewsets.ModelViewSet):
    queryset = HttpAlarmPolicy.objects.all()
    serializer_class = HttpAlarmPolicySerializer

class HttpEnvViewSet(viewsets.ModelViewSet):
    queryset = HttpEnv.objects.all()
    serializer_class = HttpEnvSerializer