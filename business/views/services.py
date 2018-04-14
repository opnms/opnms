from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Service
from users.models import User
from ..forms import ProjectForm

__all__ = ['SerivceListView']

class SerivceListView(LoginRequiredMixin,TemplateView):
    template_name = 'service/service_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Service List')
        context['services'] = Service.objects.all()
        return context

