from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django import forms
from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,SolarSchedule
# from djcelery.models import PeriodicTasks,PeriodicTask,CrontabSchedule,IntervalSchedule,WorkerState,TaskState

__all__ = ['PeriodicTaskForm','CrontabForm','IntervalForm','SolarForm']

class PeriodicTaskForm(forms.ModelForm):
    class Meta:
        model = PeriodicTasks
        fields = ()


class CrontabForm(forms.ModelForm):
    class Meta:
        model = CrontabSchedule
        fields = ('minute','hour','day_of_week','day_of_month','month_of_year')

class IntervalForm(forms.ModelForm):
    class Meta:
        model = IntervalSchedule
        fields = ('every','period')

class SolarForm(forms.ModelForm):
    class Meta:
        model = SolarSchedule
        fields = ()
        # 'event', 'latitude', 'longitude'
    # event = forms.ChoiceField()
    # latitude = forms.DecimalField( max_digits=9, decimal_places=6)
    # longitude = forms.DecimalField( max_digits=9, decimal_places=6
    # )
