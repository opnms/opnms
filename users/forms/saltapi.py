from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from ..models import UserGroup,User,Department
from django.conf import settings
from captcha.fields import CaptchaField
from captcha.models import captcha_settings
from deploy.models import SaltStack

__all__ = ['SaltApiForm']

class SaltApiForm(forms.ModelForm):
    class Meta:
        model = SaltStack
        fields = ('url','username','password','comment')


