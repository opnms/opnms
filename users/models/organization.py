#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Company(models.Model):
    name = models.CharField(max_length=150,blank=False,verbose_name=_('Company Limited'))
    address = models.CharField(max_length=150,blank=False,verbose_name=_('Address'))
    phone = models.CharField(max_length=15,verbose_name=_('Phone'))
    aa = models.ManyToOneRel

    class Meta:
        ordering = ['name']