from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import pinyin,FIRST_LETTER

__all__ = ['SaltHost','SaltGroup','SaltStack']

class SaltStack(models.Model):
    url = models.URLField(max_length=150,unique=True,verbose_name = _('Saltapi Url'))
    username = models.CharField(max_length=100,verbose_name=_('UserName'))
    password = models.CharField(max_length=100,verbose_name=_('Password'))
    comment = models.TextField(verbose_name=_('Comment'))

    def __unicode__(self):
        return self.username

    class Meta:
        default_permissions = ()
        permissions = (
            ('view_saltapi', _('view salt api')),
            ('edit_saltpai', _('Edit salt api'))
        )


class SaltHost(models.Model):
    minion = models.CharField(max_length=100,unique=True,verbose_name=_("Salt Minion"))
    alive_last_time = models.DateTimeField(auto_now=True,verbose_name=_('Alive Last Time'))

    def __unicode__(self):
        return self.minion

    class Meta:
        default_permissions =()
        permissions = (
            ('view_deploy',_('view host deploy')),
            ('edit_deploy',_('Edit host deploy')),
            ('edit_salthost',_('view salt host'))

        )

class SaltGroup(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name=_('Salt Group'))
    abbr_name = models.CharField(max_length=100,unique=True,verbose_name=_('Salt Group Abbrname'))
    minions = models.ManyToManyField(SaltHost,related_name='salt_host_set',verbose_name=_('Salt Host'))
    comment = models.TextField(blank=True,verbose_name=_('Comment'))

    def generate_abbr_name(self):
        abbr_name = pinyin(self.name)
        return abbr_name


    def __unicode__(self):
        return self.name

    class Meta:
        default_permissions = ()
        permissions = (
            ('edit_saltgroup',_('Salt Groups')),
            ('view_saltgroup',_('View SaltGroup'))
        )






