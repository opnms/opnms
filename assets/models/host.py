from django.db import models
from django.utils.translation import ugettext_lazy as _
from xpinyin import Pinyin


__all__ = ['Host']

class Host(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=_('host id'))
    name = models.CharField(max_length=70,unique=True,verbose_name=_('host name'))
    instanceName = models.CharField(max_length=70,verbose_name=_('instanceName'))
    instanceId = models.CharField(max_length=120,unique=True,blank=False,verbose_name=_('instanceId'))
    internetIp = models.CharField(max_length=15,verbose_name=_('internetIp'))
    intranetIp = models.CharField(max_length=15,verbose_name=_('intranetIp'))
    status = models.CharField(max_length=10,verbose_name=_('status'))
    connectivity = models.BooleanField(verbose_name=_('connectivity'))
    regionId = models.IntegerField(verbose_name=_('regionId'))
    regionDisplay = models.CharField(max_length=30,verbose_name=_('regionDisplay'))
    cpu = models.CharField(max_length=11,verbose_name=_('cpu'))
    cpuUsed = models.CharField(max_length=10,verbose_name=_('cpuUsed'))
    memory = models.CharField(max_length=11,verbose_name=_('memory'))
    memUsed = models.CharField(max_length=11,verbose_name=_('memUsed'))
    diskSize = models.CharField(max_length=11,verbose_name=_('diskSize'))
    diskUsed = models.CharField(max_length=11,verbose_name=_('diskUsed'))
    containerCount = models.IntegerField(verbose_name=_('containerCount'))


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']