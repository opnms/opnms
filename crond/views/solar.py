#-*-coding:utf-8 -*-

from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,SolarSchedule
from django_celery_beat.schedulers import ModelEntry,DatabaseScheduler
from celery import security,schedules,signals
from celery.app import registry
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from ..forms import SolarForm
__all__ = ['SolarCreateView','SolarUpdateView']

class SolarCreateView(LoginRequiredMixin,CreateView):
    '''
    SolarSchedule Create
    '''
    
    model = SolarSchedule
    template_name = 'solar/solar_create_update.html'
    form_class = SolarForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Solar Create')
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')

class SolarUpdateView(LoginRequiredMixin,UpdateView):
    '''
    SolarSchedule Update
    '''
    model = SolarSchedule
    form_class = SolarForm
    template_name = 'solar/solar_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Solar Update')
        context['solars'] = get_object_or_404(SolarSchedule,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')