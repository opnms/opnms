#-*-coding:utf-8 -*-

from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks,SolarSchedule
# from djcelery.models import PeriodicTask,CrontabSchedule,IntervalSchedule,PeriodicTasks
from django_celery_beat.schedulers import ModelEntry,DatabaseScheduler
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
from ..forms import PeriodicTaskForm,CrontabForm

__all__ = ['CrontabListView','CrontabCreateView','CrontabUpdateView']

class CrontabListView(LoginRequiredMixin,TemplateView):
    template_name = 'crond/crontab_list.html'
    model = CrontabSchedule
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Crontab List')
        context['crontabs'] = CrontabSchedule.objects.all()
        context['intervals'] = IntervalSchedule.objects.all()
        # context['solars'] = SolarSchedule.objects.all()
        return context

class CrontabCreateView(LoginRequiredMixin,CreateView):
    template_name = 'crond/crontab_create_update.html'
    form_class = CrontabForm
    model = CrontabSchedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Crontab Create')
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')


class CrontabUpdateView(LoginRequiredMixin,UpdateView):
    '''
    Crontab update
    '''
    template_name = 'crond/crontab_create_update.html'
    form_class = CrontabForm
    model = CrontabSchedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Crontab Update')
        context['crontabs'] = get_object_or_404(CrontabSchedule,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('crondtasks:crontab-list')


