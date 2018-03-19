from rest_framework import routers,serializers,viewsets
from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,SolarSchedule
# from djcelery.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,WorkerState,TaskState,TASK_STATE_CHOICES
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

__all__ = ['PeriodicTaskSerializer','CrontabScheduleSerializer','IntervalScheduleSerializer','SolarScheduleSerializer']

class PeriodicTaskSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = '__all__'

class CrontabScheduleSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = '__all__'

class IntervalScheduleSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = '__all__'


class SolarScheduleSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    class Meta:
        model = SolarSchedule
        fields = '__all__'

