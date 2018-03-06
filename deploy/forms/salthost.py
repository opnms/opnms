from __future__ import unicode_literals

from django import forms
from ..models import SaltHost,SaltGroup


__all__ = ['SaltHostForm','SaltGroupForm']


class SaltHostForm(forms.ModelForm):
    '''
    salt host form
    '''

    class Meta:
        model = SaltHost
        fields = ['minion']

class SaltGroupForm(forms.ModelForm):
    '''
    salt group forms
    '''
    class Meta:
        model = SaltGroup
        fields = ('name','minions','comment')
