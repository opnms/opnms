from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import pinyin,lazy_pinyin,FIRST_LETTER

__all__ = ['HttpAlarmPolicy','HttpMonitorGroup','HttpMonitor','HttpEnv']


class HttpAlarmPolicy(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('alarm policy'))
    code = models.CharField(max_length=5, verbose_name=_('status code'))
    timeout = models.CharField(max_length=10, verbose_name=_('timeout'))
    step = models.CharField(max_length=5, verbose_name=_('max_step'))
    times = models.CharField(max_length=5, blank=True, null=True, verbose_name=_('times'))
    keywords = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('keywords'))
    create_by = models.CharField(max_length=50, blank=False, verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create at'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['create_at']


class HttpMonitorGroup(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('http group'))
    comment = models.TextField(blank=True, null=True, verbose_name=_('comment'))
    create_by = models.CharField(max_length=50, blank=False, verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create at'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HttpMonitor(models.Model):
    name = models.URLField(verbose_name=_('http url'),db_index=True)
    service = models.CharField(max_length=50,blank=False,verbose_name=_('desc'))
    alarmploicy = models.ForeignKey(HttpAlarmPolicy, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name=_('http alarm policy'))
    group = models.ForeignKey(HttpMonitorGroup,on_delete=models.SET_NULL,blank=True,null=True,verbose_name=_('http group'))
    comment = models.TextField(blank=True,null=True,verbose_name=_('comment'))
    create_by = models.CharField(max_length=50, blank=False, verbose_name=_('Create by'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create at'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['service']



class HttpEnv(models.Model):
    name = models.CharField(max_length=5,blank=False,null=False,verbose_name=_('env url'))
    status = models.CharField(max_length=5,blank=False,null=False,verbose_name=_('status'))
    ipaddress = models.CharField(max_length=20,verbose_name=_('IPAddress'))
    event_time = models.IntegerField(verbose_name=_('event time'))
    resp_time = models.IntegerField(verbose_name=_('response time'))
    resp_code = models.IntegerField(verbose_name=_('code'))
    result = models.IntegerField(verbose_name=_('result'))
    currentstep =  models.IntegerField(verbose_name=_('current step'))
    maxstep = models.IntegerField(verbose_name=_('max step'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['event_time']

class Http(models.Model):
    name = models.CharField(max_length=50,unique=True,verbose_name=_('http name'))
    url = models.URLField(verbose_name=_('http url'))
