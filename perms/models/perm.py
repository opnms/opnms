from django.db import models
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _

__all__ = ['Perm']

class Perm(Permission):

    create_by = models.CharField(max_length=100,verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create at'))