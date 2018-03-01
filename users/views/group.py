#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView,DeleteView, FormMixin, FormView
)
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout

from ..forms import GroupFrom
from ..models import UserGroup

__all__ = ['GroupCreateView','GroupUpdateView','GroupDeleteView']

class GroupCreateView(LoginRequiredMixin,CreateView):
    template_name = 'groups/create_group.html'
    form_class = GroupFrom
    model = UserGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create Group')
        return context

    def form_valid(self, form):
        usergroup = form.save(commit=False)
        usergroup.create_by = self.request.user.username
        usergroup.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class GroupUpdateView(LoginRequiredMixin,UpdateView):
    model = UserGroup
    form_class = GroupFrom
    template_name = 'groups/update_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Update Group')
        context['groups'] = get_object_or_404(UserGroup,pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        usergroup = form.save(commit=False)
        usergroup.create_by = self.request.user.username
        usergroup.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class GroupDeleteView(LoginRequiredMixin,DeleteView):
    model = UserGroup

    def delete(self, request, *args, **kwargs):
        return super().delete(request,*args,**kwargs)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

