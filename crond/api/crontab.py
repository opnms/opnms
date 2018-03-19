from rest_framework import routers,viewsets
from django_celery_beat.models import CrontabSchedule
# from djcelery.models import CrontabSchedule
from ..serializers import CrontabScheduleSerializer


__all__ = ['CrontabViewSet']

class CrontabViewSet(viewsets.ModelViewSet):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer
