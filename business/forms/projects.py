from __future__ import unicode_literals

from django import forms
from ..models import Project
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


__all__ = ['ProjectForm']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','abbr_name','owner','code_address','comment')