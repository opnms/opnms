from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
from .service import Service

__all__ = ['Project','ProjectEnv']

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
    env_chocies = (
        ('prod','生产环境'),
        ('pre', '预发环境')
    )
    name = models.CharField(max_length=5,choices=env_chocies,verbose_name=_('env'))
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name=_('Project'))
    service = models.OneToOneField(Service,on_delete=models.CASCADE,verbose_name=_('service'))

    def __unicode__(self):
        return self.project

    class Meta:
        ordering = ['project']
        unique_together = (('name', 'project','service'),)