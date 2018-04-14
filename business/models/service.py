from django.db import models
from users.models import User
from jsonfield import JSONField
from django.utils.translation import ugettext_lazy as _

__all__ = ['Service']

class Service(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=_('Service ID'))
    name = models.CharField(max_length=50,unique=True,verbose_name=_('Service Name'))
    imageName = models.CharField(max_length=100,verbose_name=_('Image Name'))
    createTime = models.CharField(max_length=120,verbose_name=_('Create at'))
    regionDisplay = models.CharField(max_length=50,verbose_name=_('Region'))
    nodes = JSONField(verbose_name=_('Node List'))

    def __unicode__(self):
        return  self.name

    class Meta:
        permissions = (
            ('view_service', _('view service')),
            ('refresh_service', _('refresh serice'))
        )