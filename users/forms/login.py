#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
from django.views.generic.edit import TemplateResponseMixin



__all__ = ['UserLoginForm',]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,label=_('Username'),strip=True)
    password = forms.CharField(max_length=50,strip=False,label=_('Password'),widget=forms.TextInput)
    error_messages = {'invalid_login':_('Please enter a correct username and password.'),
                      'inactive': _("This account is inactive."),
                      }
    #登录页验证码
    captcha = CaptchaField()

# class UserRegiesterForm()




