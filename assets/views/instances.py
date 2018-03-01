from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from ..tasks import ecs_sync
from ..models import Instance

__all__ = ['InstanceListView','InstanceDetailView','InstanceRefreshView']

class InstanceListView(LoginRequiredMixin,TemplateView):
    template_name = 'instances/instance_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('InstanceList')
        context['instances'] = Instance.objects.all()
        return context

class InstanceRefreshView(LoginRequiredMixin,TemplateView):
    '''
    refresh ecs infomation
    '''
    template_name = 'instances/instance_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ecs_sync()
        context['action'] = _('InstanceList')
        context['instances'] = Instance.objects.all()
        return context



class InstanceDetailView(LoginRequiredMixin,DetailView):
    template_name = 'instances/instance_detail.html'
    model = Instance
    context_object_name = 'instance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Instance Detail')
        context['instances'] = get_object_or_404(Instance,pk=self.kwargs['pk'])
        return context



