from __future__ import unicode_literals

from django import forms
from ..models import SaltHost,SaltGroup,SaltModule


__all__ = ['SaltHostForm','SaltGroupForm','SaltModuleForm']


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

class SaltModuleForm(forms.ModelForm):
    '''
    salt module forms
    '''

    class Meta:
        model = SaltModule
        fields = ('name','comment')
