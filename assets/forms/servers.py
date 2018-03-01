from __future__ import unicode_literals

from django import forms
from ..models import Server
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

__all__ = ['ServerForm']

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ()