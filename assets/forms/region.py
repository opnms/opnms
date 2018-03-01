from __future__ import unicode_literals

from django import forms
from ..models import Region
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


__all__ = ['RegionForm']


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('name','provider','city')

