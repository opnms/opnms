from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Region,Cloudprovider,Instance
from ..forms import RegionForm

__all__= ['RegionListView','RegionCreateView','RegionUpdateView']

class RegionListView(LoginRequiredMixin,TemplateView):
    template_name = 'region/region_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('RegionList')
        context['regions'] = Region.objects.all()
        context['Cloudproviders'] = Cloudprovider.objects.all()
        return context

class RegionCreateView(LoginRequiredMixin,CreateView):
    template_name = 'region/create_update.html'
    model = Region
    form_class = RegionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create Region')
        context['Cloudproviders'] = Cloudprovider.objects.all()
        return context

    def form_valid(self,form):
        region = form.save(commit=False)
        region.create_by = self.request.user.username
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('assets:region-list')


class RegionUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'region/create_update.html'
    model = Region
    form_class = RegionForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Update Region')
        context['regions'] = get_object_or_404(Region,pk=self.kwargs['pk'])
        context['Cloudproviders'] = Cloudprovider.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('assets:region-list')
