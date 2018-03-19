from rest_framework import routers,viewsets
from django_celery_beat.models import SolarSchedule
from ..serializers import SolarScheduleSerializer


__all__ = ['SolarScheduleViewSet']

class SolarScheduleViewSet(viewsets.ModelViewSet):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer