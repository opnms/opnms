#-*-coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['Department']

class Department(models.Model):
    name = models.CharField(max_length=30,unique=True,blank=False,default='guest',verbose_name=_('Department'))
    # principal = models.ManyToManyField(User,related_name='users',verbose_name=_('Principal'))
    comment= models.TextField(null=False,blank=True,verbose_name=_('Comment'))
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Create at'))
    create_by = models.CharField(max_length=50, default='admin')
