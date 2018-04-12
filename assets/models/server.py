from django.db import models
from deploy.models import SaltHost
from django.utils.translation import ugettext_lazy as _
from .instances import Instance
from xpinyin import Pinyin

__all__ = ['Server']

class Server(models.Model):
    hostname = models.CharField(max_length=100,unique=True,blank=True,null=True,verbose_name=_('HostName'))
    inneripaddress = models.CharField(max_length=20,unique=True,blank=True,verbose_name=_('InnerIpAddress'))
    publicipaddress = models.CharField(max_length=25, blank=True, verbose_name=_('PublicIpAddress'))
    serialnumber = models.CharField(max_length=50, verbose_name=_('SerialNumber'))
    manufacturer = models.CharField(max_length=20, blank=True, verbose_name=_('manufacturer'))
    productname = models.CharField(max_length=30, blank=True,verbose_name=_('productname'))
    osrelease = models.CharField(max_length=25, verbose_name=_('os'), blank=True, null=True)
    cpu_model = models.CharField(max_length=100, blank=True, verbose_name=_('cpu_model'))
    num_cpus = models.PositiveSmallIntegerField(verbose_name=_('cpu_nums'), blank=True, null=True)
    num_gpus = models.PositiveSmallIntegerField(verbose_name=_('gpu_nums'), blank=True, null=True)
    memory = models.CharField(max_length=20, blank=True, verbose_name=_('Memory'))
    hd = models.TextField(blank=True,verbose_name=_('hd'))
    nic = models.TextField(blank=True, verbose_name=_('nic'))
    virtual = models.CharField(max_length=20, blank=True, verbose_name=_('virtual'))
    kernelrelease = models.CharField(max_length=200, blank=True, verbose_name=_('kernel'))
    shell = models.CharField(max_length=10, blank=True, verbose_name=_('shell'))
    saltversion = models.CharField(max_length=10, blank=True, verbose_name=_('saltversion'))
    locale = models.CharField(max_length=200, blank=True, verbose_name=_('locale'))
    selinux = models.CharField(max_length=50, blank=True, verbose_name=_('selinux'))
    lastupdate = models.DateTimeField(auto_now=True,verbose_name=_('LastUpdat_time'))
    create_by = models.CharField(max_length=50,blank=False,verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Create at'))

    def __unicode__(self):
        return self.hostname

    class Meta:
        ordering = ['hostname']

    def generate_hostname(self):
        instanceName = Instance.objects.filter(
            SerialNumber=self.serialnumber,
        )
        pinyin = Pinyin()
        info = instanceName[0].InstanceName
        innerIP = instanceName[0].InnerIpAddress[0]
        pubIP = instanceName[0].PublicIpAddress[0]
        if not info:
            raise ValueError

        else:
            info = instanceName[0].InstanceName.split("-")
            hostname_last = Server.objects.filter(
                hostname__regex= r'^%s[0-9]{3}.meetyima.com$' %(pinyin.get_pinyin(info[0],'') + '-' + info[1] + '-' + info[2]  + '-')
            ).order_by('hostname').last()

            #如果查到有同名主机名,id加1,否则id为001
            print(hostname_last)
            if hostname_last:
                hostname_last_id = str(hostname_last[0].hostname.split("-")[3].split(".")[0] + 1).zfill(3)
                print(hostname_last_id)
            else:
                hostname_last_id = '001'
            hostname = pinyin.get_pinyin(info[0], '') + '-' + info[1] + '-' + info[2] + '-' + hostname_last_id + '.' + 'meetyima.com'
        return hostname,innerIP,pubIP

    def save(self, *args,**kwargs):
        if not self.hostname:
            self.hostname,self.inneripaddress,self.publicipaddress = self.generate_hostname()
        return super().save(*args,**kwargs)

