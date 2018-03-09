from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['Cloudprovider','Region']


class Cloudprovider(models.Model):
    '''
    Cloud service provider
    '''
    name = models.CharField(max_length=30,unique=True,verbose_name=_('IDC Name'))
    keyid = models.CharField(max_length=50,verbose_name=_('Key ID'))
    keysecret = models.CharField(max_length=50,verbose_name=_('Secret'))
    abbr_name = models.SlugField(max_length=15,unique=True,blank=True,null=True,verbose_name=_('Abbr Slug'))
    country = models.CharField(max_length=5,default='CN',verbose_name=_("Country"))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create at'))
    create_by = models.CharField(max_length=100,blank=False,verbose_name=_('Create by'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Region(models.Model):
    name = models.CharField(max_length=15,verbose_name=_('Region'))
    provider = models.ForeignKey(Cloudprovider,on_delete=models.CASCADE,verbose_name=_('Cloud Provider'))
    city = models.CharField(max_length=15, blank=False, verbose_name=_('City'))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create at'))
    create_by = models.CharField(max_length=100,blank=False,verbose_name=_('Create by'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering =['name']
        unique_together = (('name','provider'),)