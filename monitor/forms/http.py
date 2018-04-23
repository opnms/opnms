from __future__ import unicode_literals

from django import forms
from ..models import HttpMonitor,HttpEnv,HttpAlarmPolicy,HttpMonitorGroup

__all__ = ['HttpMonitorForm','HttpAlarmPolicyForm','HttpMonitorGroupForm']

class HttpMonitorForm(forms.ModelForm):
    class Meta:
        model = HttpMonitor
        fields = ('name','service','alarmploicy','group','comment')

class HttpAlarmPolicyForm(forms.ModelForm):
    class Meta:
        model = HttpAlarmPolicy
        fields = ('name','code','timeout','step','times','keywords')

class HttpMonitorGroupForm(forms.ModelForm):
    class Meta:
        model = HttpMonitorGroup
        fields = ('name','comment')