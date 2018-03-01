# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from base.system import UserPassesTestMixin
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

from ..forms import CreateUserForm,UpdateUserForm
from ..models import User, UserGroup,Department
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


__all__ = ['UserListView','UserDetailView','UserCreateView','UserInfoUpdateView','UserDeleteView','UserProfileView']


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_list.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app'] = _('Users')
        context['action'] = _('user list')
        context['users'] = User.objects.all()
        context['groups'] = UserGroup.objects.all()
        context['deaprtments'] = Department.objects.all()
        return context

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        groups = UserGroup.objects.exclude(id__in=self.object.groups.all())
        context = {
            'action': _('User detail'),
            'groups': groups
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

class UserCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'users/create_update_user.html'
    form_class = CreateUserForm
    model = User
    success_message = '%s create success.' % (User.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Create User')
        context['groups'] = UserGroup.objects.all()
        context['departments'] = Department.objects.all()
        return context

    def form_valid(self, form):

        user = form.save(commit=False)
        user.create_by = self.request.user.username or 'Administrator'
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class UserInfoUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'users/update_user.html'
    model = User
    form_class = UpdateUserForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = UserGroup.objects.all()
        context['departments'] = Department.objects.all()
        context['users'] = get_object_or_404(User,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('User Delete')
        return context

    def get_success_url(self):
        return reverse_lazy('users:user-list')

class UserProfileView(LoginRequiredMixin,TemplateView):
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('User Profile')
        context['userinfo'] = get_object_or_404(User,pk=self.kwargs['pk'])
        return context


