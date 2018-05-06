from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from ..models import UserGroup,User,Department
from django.conf import settings
from captcha.fields import CaptchaField
from captcha.models import captcha_settings

__all__ = ['CreateUserForm','UpdateUserForm']


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','phone','department','groups','wechat','dingding','job_number']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','phone','department','groups','wechat','dingding']

class ForgotPasswordView(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
