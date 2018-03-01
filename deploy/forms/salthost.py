from __future__ import unicode_literals

from django import forms
from ..models import SaltHost


__all__ = ['SlatHostForm']


class SlatHostForm(forms.ModelForm):
    '''
    salt host form
    '''

    class Meta:
        model = SaltHost
        fields = ['minion']