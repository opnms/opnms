#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
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

from ..forms import DepartMentForm
from ..models import Department

__all__ = ['DepartmentListView','DepartmentCreateView','DeaprtmentUpdateView','DepartmentDeleteView']


class DepartmentListView(LoginRequiredMixin,TemplateView):
    template_name = 'users/user_list.html'
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('DepartmentList')
        context['depart'] = Department.objects.all()
        return context

class DepartmentCreateView(LoginRequiredMixin,CreateView):
    template_name = 'department/create_department.html'
    form_class = DepartMentForm
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create Department')
        return context

    def form_valid(self, form):
        department= form.save(commit=False)
        department.create_by = self.request.user.username
        department.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class DeaprtmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Department
    form_class = DepartMentForm
    template_name = 'department/update_department.html'
    success_message = 'Department update success.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Update department')
        return context

    def form_valid(self, form):
        department = form.save(commit=False)
        department.create_by = self.request.user.username
        department.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class DepartmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Delete Department')
        return context

    def delete(self, request, *args, **kwargs):
        return super().delete(request,*args,**kwargs)

    def get_success_url(self):
        return reverse_lazy('users:user-list')