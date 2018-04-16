from django.db import models
from django.utils.translation import ugettext_lazy as _
from xpinyin import Pinyin


__all__ = ['Container']


class Container(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=_('container id'))
    nodeId = models.IntegerField(blank=False,verbose_name=_('node id'))
    status = models.CharField(max_length=30,verbose_name=_('container status'))
    createTime = models.CharField(max_length=50,verbose_name=_('createTime'))
    startTime = models.CharField(max_length=50,blank=True,null=True,verbose_name=_('startTime'))
    stopTime = models.CharField(max_length=50,blank=True,null=True,verbose_name=_('stopTime'))
    hostId = models.IntegerField(blank=False,verbose_name=_('hostId'))
    cpu = models.CharField(max_length=5,verbose_name=_('cpu'))
    mem = models.CharField(max_length=8,verbose_name=_('mem'))
    disk = models.CharField(max_length=8,verbose_name=_('disk'))
    health = models.CharField(max_length=10,blank=True,null=True,verbose_name=_('health'))


    def __unicode__(self):
        return self.health

    class Meta:
        ordering = ['id']