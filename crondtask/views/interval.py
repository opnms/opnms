#-*-coding:utf-8 -*-

from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,SolarSchedule
# from djcelery.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks
# from djcelery.schedulers import ModelEntry,DatabaseScheduler
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
from ..forms import IntervalForm
__all__ = ['IntervalCreateView','IntervalUpdateView']

class IntervalCreateView(LoginRequiredMixin, CreateView):
    '''
    IntervalSchedule create
    '''

    model = IntervalSchedule
    form_class = IntervalForm
    template_name = 'interval/interval_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Interval Create')
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')

class IntervalUpdateView(LoginRequiredMixin,UpdateView):
    '''
    Interval update view
    '''
    model = IntervalSchedule
    form_class = IntervalForm
    template_name = 'interval/interval_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Interval Update')
        context['intervals'] = get_object_or_404(IntervalSchedule,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')
