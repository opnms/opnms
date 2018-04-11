from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _

__all__ = ['Project']

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name=_('project name'))
    abbr_name = models.SlugField(max_length=50,unique=True,verbose_name=_('project abbr name'))
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name=_('project owner'))
    code_address = models.URLField(verbose_name=_('gitlab url'))
    comment = models.TextField(blank=True,verbose_name=_("Comment"))
    create_by = models.CharField(max_length=50, blank=False, verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create at'))

    def __unicode__(self):
        return self.name

    class Mete:
        permissions = (
            ('view_project', _('view project')),
            ('edit_project', _('Edit project')),
            ('deploy_project', _('deploy project'))
        )



class ProjectEnv(models.Model):
    name = models.CharField(max_length=100)