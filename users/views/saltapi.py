#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView,DeleteView, FormMixin, FormView
)
from django.views.generic.detail import DetailView
from ..forms import SaltApiForm
from deploy.models import SaltStack

__all__ = ['SaltApiListView','SaltApiCreateView','SaltApiUpdateView']


class SaltApiListView(LoginRequiredMixin,TemplateView):
    template_name = 'saltapi/saltapi-list.html'
    model = SaltStack

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('SaltApi List')
        context['saltapis'] = SaltStack.objects.all()
        return context



class SaltApiCreateView(LoginRequiredMixin,CreateView):
    model = SaltStack
    form_class = SaltApiForm
    template_name = 'saltapi/saltapi_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create SaltApi')
        return context

    def get_success_url(self):
        return reverse_lazy('users:saltapi-list')


class SaltApiUpdateView(LoginRequiredMixin,UpdateView):
    model = SaltStack
    form_class = SaltApiForm
    template_name = 'saltapi/saltapi_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('SaltApi Update')
        context['saltapi'] = get_object_or_404(SaltStack,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('users:saltapi-list')