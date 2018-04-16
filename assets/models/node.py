from django.db import models
from django.utils.translation import ugettext_lazy as _
from xpinyin import Pinyin
import jsonfield

__all__ = ['Node']

class Node(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=_('nodeId'))
    name = models.CharField(max_length=30,verbose_name=_('nodeName'))
    imageName = models.CharField(max_length=50,verbose_name=_('imageName'))
    status = models.CharField(max_length=15,verbose_name=_('status'))
    serviceId = models.IntegerField(verbose_name=_('serviceId'))
    createTime = models.CharField(max_length=70,verbose_name=_('createTime'))
    containers = jsonfield.JSONField(verbose_name=_('containers'))


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['id']