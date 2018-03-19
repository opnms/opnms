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


__all__ = ['PeriodicTasksListView','PeriodicTaskDetailVeiw','PeriodicTaskCreateView']


class PeriodicTasksListView(LoginRequiredMixin,TemplateView):
    '''
    crontab list
    '''
    template_name = 'periodic/periodictask_list.html'
    # model = PeriodicTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Task List')
        context['tasks'] = PeriodicTask.objects.all()
        return context

class PeriodicTaskDetailVeiw(LoginRequiredMixin,DetailView):
    '''
    crontab Detail
    '''
    template_name = 'crond/periodictask_list.html'
    model = PeriodicTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('PeriodicTasks Detail')
        return context

class PeriodicTaskCreateView(LoginRequiredMixin,CreateView):
    '''
    crontab create view
    '''
    pass