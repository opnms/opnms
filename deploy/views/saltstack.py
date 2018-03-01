from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import SaltHost,SaltGroup
from ..saltstack.saltapi import SalstStack
from ..forms import SaltGroupForm,SaltHostForm

__all__ = ['SalstHostListView']

class SalstHostListView(LoginRequiredMixin,TemplateView):
    '''
    salt host and group view.
    '''
    template_name = 'saltstack/hostlist.html'
    model = SaltHost

    def get_context_data(self, **kwargs):
        '''
        get all host and group to salt host list.
        :param kwargs:
        :return: action,salt host and salt group
        '''
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Key List')
        context['hostlist'] = SaltHost.objects.all()
        context['hostgroups'] = SaltGroup.objects.all()
        return context

class SaltGroupCreateView(LoginRequiredMixin,CreateView):
    '''
    salt group create.
    '''
    template_name = 'saltstack/saltgroup_create_update.html'
    model = SaltGroup
    form_class = SaltGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('salt group create')
        context['salthosts'] = SaltHost.objects.all()
        return context

    def get_success_url(self):
        reverse_lazy('deploys:saltapi-list')


class SaltGroupUpdateView(LoginRequiredMixin,UpdateView):
    '''
    salt group update
    '''
    template_name = 'saltstack/saltgroup_create_update.html'
    model = SaltGroup
    form_class = SaltGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('salt group update')
        context['salthosts'] = SaltHost.objects.all()
        context['saltgroup'] = get_object_or_404(SaltGroup,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        reverse_lazy('deploys:saltapi-list')
