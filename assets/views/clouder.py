from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Cloudprovider
from ..forms import CloudProviderForm

__all__ = ['CloudProviderCreateView','CloudProviderUpdateView','CloudeProviderDeleteView']


class CloudProviderCreateView(LoginRequiredMixin,CreateView):
    '''
    cloud create func
    '''
    model = Cloudprovider
    form_class = CloudProviderForm
    template_name = 'cloudprovider/cloud_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create Cloudprovider')
        return context

    def form_valid(self, form):
        cloud = form.save(commit=False)
        cloud.create_by = self.request.user.username
        cloud.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('assets:region-list')


class CloudProviderUpdateView(LoginRequiredMixin,UpdateView):
    '''
    cloud update func
    '''
    model = Cloudprovider
    form_class = CloudProviderForm
    template_name = 'cloudprovider/cloud_create_update.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        cloud = form.save(commit=False)
        cloud.create_by = self.request.user.username
        cloud.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Update Cloudprovider')
        context['cloudes'] = get_object_or_404(Cloudprovider,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('assets:region-list')


class CloudeProviderDeleteView(LoginRequiredMixin,DeleteView):
    '''
    cloud delete func
    '''
    model = Cloudprovider
    template_name = 'cloudprovider/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Delete Provider')
        return context

    def get_success_url(self):
        return reverse_lazy('assets:region-list')
