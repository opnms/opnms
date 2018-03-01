from django.db import models
from deploy.models import SaltHost
from django.utils.translation import ugettext_lazy as _

__all__ = ['Server']

class Server(models.Model):
    hostname = models.CharField(max_length=50,unique=True,verbose_name=_('HostName'))
    inneripaddress = models.CharField(max_length=20,verbose_name=_('InnerIpAddress'))
    publicipaddress = models.CharField(max_length=25, verbose_name=_('PublicIpAddress'))
    serialnumber = models.CharField(max_length=50, unique=True, verbose_name=_('SerialNumber'))
    manufacturer = models.CharField(max_length=20, verbose_name=_('manufacturer'))
    productname = models.CharField(max_length=30, verbose_name=_('productname'))
    esc = models.CharField(max_length=20, verbose_name=_('esc'), blank=True, unique=True, null=True)
    os = models.CharField(max_length=25, verbose_name=_('os'), blank=True, null=True)
    purchase_date = models.DateField(verbose_name=_('purchase_date'), blank=True, null=True)
    maintain = models.BooleanField(verbose_name=_('maintain'), default=False)
    cpu_model = models.CharField(max_length=100, blank=True, verbose_name=_('cpu_model'))
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=_('cpu_nums'), blank=True, null=True)
    memory = models.CharField(max_length=20, verbose_name=_('Memory'))
    hd = models.TextField(blank=True, verbose_name=_('hd'))
    nic = models.TextField(blank=True, verbose_name=_('nic'))
    virtual = models.CharField(max_length=20, blank=True, verbose_name=_('virtual'))
    kernel = models.CharField(max_length=200, blank=True, verbose_name=_('kernel'))
    shell = models.CharField(max_length=10, blank=True, verbose_name=_('shell'))
    saltversion = models.CharField(max_length=10, blank=True, verbose_name=_('saltversion'))
    locale = models.CharField(max_length=200, blank=True, verbose_name=_('locale'))
    selinux = models.CharField(max_length=50, blank=True, verbose_name=_('selinux'))
    lastupdate = models.DateTimeField(auto_now=True,verbose_name=_('LastUpdat_time'))
    minion = models.ForeignKey(SaltHost,on_delete=True,verbose_name=_('Salt Minion'))
    create_by = models.CharField(max_length=50,blank=False,verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create at'))

    def __unicode__(self):
        return self.hostname

    class Meta:
        ordering = ['hostname']