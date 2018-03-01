from __future__ import unicode_literals

from django import forms
from ..models import Cloudprovider

__all__ = ['CloudProviderForm']

class CloudProviderForm(forms.ModelForm):
    class Meta:
        model = Cloudprovider
        fields = ('name','keyid','keysecret','country','abbr_name')