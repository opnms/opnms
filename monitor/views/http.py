from __future__ import unicode_literals

import json
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.views.generic.detail import DetailView
from ..models import HttpMonitor,HttpMonitorGroup,HttpAlarmPolicy,HttpEnv
from ..forms import HttpAlarmPolicyForm,HttpMonitorForm,HttpMonitorGroupForm

__all__ = ['HttpMonitorListView','HttpMonitorCreateView','HttpMonitorUpdateView']

class HttpMonitorListView(LoginRequiredMixin,TemplateView):
    template_name = 'httpmonitor/http_list.html'
    model = HttpMonitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('httpmonitor list')
        context['httpmonitors'] =HttpMonitor.objects.all()
        return context


class HttpMonitorCreateView(LoginRequiredMixin,CreateView):
    template_name = 'httpmonitor/http_create_update.html'
    model = HttpMonitor
    form_class = HttpMonitorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('httpmonitor create')
        context['groups'] = HttpMonitorGroup.objects.all()
        context['alarms'] = HttpAlarmPolicy.objects.all()

        return context

    def form_valid(self, form):
        httpmonitor = form.save(commit=False)
        httpmonitor.create_by = self.request.user.username
        httpmonitor.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('monitor:monitor-http-list')


class HttpMonitorUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'httpmonitor/http_create_update.html'
    model = HttpMonitor
    form_class = HttpMonitorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('httpmonitor update')
        context['contexts'] = get_object_or_404(HttpMonitor,pk=self.kwargs['pk'])
        context['groups'] = HttpMonitorGroup.objects.all()
        context['alarms'] = HttpAlarmPolicy.objects.all()
        return context

    def form_valid(self, form):
        httpmonitor = form.save(commit=False)
        httpmonitor.create_by = self.request.user.username
        httpmonitor.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('monitor:monitor-http-list')

class MonitorCreateView(LoginRequiredMixin,FormView):
    def post(self, request, *args, **kwargs):
        assert self.request.is_ajax()
        request_data = json.loads(self.request.body)
