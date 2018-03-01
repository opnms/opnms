# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.views import LoginView,LogoutView
from ..forms import UserLoginForm



__all__ = ['UserLoginView','UserLogoutView']

http_method_names = ['post','get']

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

class UserLogoutView(LogoutView):
    pass





