from rest_framework import routers,viewsets
from django_celery_beat.models import IntervalSchedule
# from djcelery.models import IntervalSchedule
from ..serializers import IntervalScheduleSerializer


__all__ = ['IntervalViewSet']

class IntervalViewSet(viewsets.ModelViewSet):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer