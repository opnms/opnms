
#-*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.core import signing
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse

from .group import UserGroup
from .department import Department

__all__ = ['User']

class User(AbstractUser):
    groups = models.ManyToManyField(UserGroup,related_name='users',verbose_name=_('User Group'))
    phone = models.CharField(blank=True,max_length=11,verbose_name=_('Phone'))
    wechat = models.CharField(blank=True,max_length=30,verbose_name=_('Wechat'))
    dingding = models.CharField(blank=True,max_length=25,verbose_name=_('dingding'))
    job_number = models.CharField(max_length=10,blank=False,verbose_name=_('Job number'))
    department = models.ManyToManyField(Department,verbose_name=_('Department'))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create time'))
    create_by = models.CharField(max_length=30,default='admin',verbose_name=_('Create by'))

    @property
    def password_raw(self):
        raise AttributeError('Password raw is not a readable attribute')

    @password_raw.setter
    def password_raw(self,password_raw):
        self.set_password(password_raw)

    def get_absolute_url(self):
        return reverse('users:user-list',self.pk)


    class Meta:
        ordering = ['username']
        permissions = (
            ('view_user','Can see available users'),
            ('change_user_status','Can change the status of users'),
            ('close_user','Can remove a user by setting its status as closed')
        )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)