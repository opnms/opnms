#-*-coding:utf-8 -*-
from django.db import models,IntegrityError
from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


__all__ = ['UserGroup']

class UserGroup(models.Model):
    '''user group model'''
    name = models.CharField(max_length=25,unique=True,verbose_name=_('GroupName'))
    comment = models.TextField(blank=True,verbose_name=_("Comment"))
    create_at = models.DateTimeField(auto_now_add=True,null=True,verbose_name=_('Create at'))
    create_by = models.CharField(max_length=50,default='admin')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


