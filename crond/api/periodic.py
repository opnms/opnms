from rest_framework import routers,viewsets
from django_celery_beat.models import PeriodicTasks,PeriodicTask
# from djcelery.models import PeriodicTask,PeriodicTasks
from ..serializers import PeriodicTaskSerializer


__all__ = ['PeriodicTasksViewSet']

class PeriodicTasksViewSet(viewsets.ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer