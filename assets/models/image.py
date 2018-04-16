from django.db import models
from deploy.models import SaltHost
from django.utils.translation import ugettext_lazy as _
from .instances import Instance
from xpinyin import Pinyin

__all__ = ['Image']

class Image(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=_('image id'))
    imageName = models.CharField(max_length=150,verbose_name=_('imageName'))
    imageTag = models.CharField(max_length=50,verbose_name=_('imageTag'))
    imageAlias = models.CharField(max_length=100,verbose_name=_('imageAlias'))
    ImageModifyTime = models.CharField(max_length=100,verbose_name=_('ImageModifyTime'))

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ['id']


