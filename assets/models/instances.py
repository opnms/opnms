from django.db import models
from jsonfield import JSONField
from django.utils.translation import ugettext_lazy as _
from .region import Region
__all__ =['Instance']


class Instance(models.Model):
    InstanceType = models.CharField(max_length=50,blank=True,verbose_name=_('InstanceType'))
    InstanceId = models.CharField(max_length=50,verbose_name=_('InstanceID'))
    SerialNumber = models.CharField(max_length=50,unique=True,verbose_name=_('SerialNumber'))
    ImageId = models.CharField(max_length=70,verbose_name=_('Image ID'))
    InstanceTypeFamily = models.CharField(max_length=50,verbose_name=_('InstanceTypeFamily'))
    VlanId = models.CharField(max_length=50,blank=True,verbose_name=_('VlanId'))
    InternetMaxBandwidthIn = models.CharField(max_length=10,blank=False,verbose_name=_('InternetMaxBandwidthIn'))
    ZoneId = models.CharField(max_length=15,blank=True,verbose_name=_('Zone'))
    InternetChargeType = models.CharField(max_length=50,verbose_name=_('InternetChargeType'))
    SpotStrategy = models.CharField(max_length=50,verbose_name=_('SpotStrategy'))
    StoppedMode = models.CharField(max_length=50,verbose_name=_('StoppedMode'))
    IoOptimized = models.BooleanField(verbose_name=_('IoOptimized'))
    Memory = models.CharField(max_length=50,verbose_name=_('Memory'))
    Cpu = models.CharField(max_length=10,verbose_name=_('Cpu'))
    DeviceAvailable = models.BooleanField(max_length=50,verbose_name=_('DeviceAvailable'))
    SaleCycle = models.CharField(max_length=50,blank=True,verbose_name=_('SaleCycle'))
    SpotPriceLimit = models.CharField(max_length=20,verbose_name=_('SpotPriceLimit'))
    AutoReleaseTime = models.CharField(max_length=50,blank=True,verbose_name=_('AutoReleaseTime'))
    StartTime = models.CharField(max_length=50,verbose_name=_('StartTime'))
    InstanceName = models.CharField(max_length=100,verbose_name=_('InstanceName'))
    Description = JSONField(max_length=50,blank=True,verbose_name=_('Description'))
    ResourceGroupId = models.CharField(max_length=50,blank=True,verbose_name=_('ResourceGroupId'))
    OSType = models.CharField(max_length=25,verbose_name=_('OSType'))
    OSName = models.CharField(max_length=50,verbose_name=_('OSName'))
    InstanceNetworkType = models.CharField(max_length=25,verbose_name=_('InstanceNetworkType'))
    HostName = models.CharField(max_length=50,blank=False,verbose_name=_('HostName'))
    CreationTime = models.CharField(max_length=50,verbose_name=_('CreationTime'))
    Status = models.CharField(max_length=15,verbose_name=_('Status'))
    ClusterId = models.CharField(max_length=50,blank=True,verbose_name=_('ClusterId'))
    GPUSpec = models.CharField(max_length=25,blank=True,verbose_name=_('GPUSpec'))
    InnerIpAddress = JSONField(blank=True,verbose_name=_('InnerIpAddress'))
    PublicIpAddress = JSONField(blank=True,default=[],verbose_name=_('PublicIpAddress'))
    SecurityGroupIds = JSONField(blank=True,default=[],verbose_name=_('SecurityGroupIds'))
    ExpiredTime = models.CharField(max_length=50,verbose_name=_('ExpiredTime'))
    EipAddress = JSONField(blank=True,default=[],verbose_name=_('EipAddress'))
    VpcAttributes = JSONField(blank=True,default=[],verbose_name=_('VpcAttributes'))
    InternetMaxBandwidthOut = models.CharField(max_length=15,verbose_name=_('InternetMaxBandwidthOut'))
    Recyclable = models.BooleanField(verbose_name=_('Recyclable'))
    RegionId = models.CharField(max_length=25,verbose_name=_('RegionId'))
    OperationLocks = JSONField(blank=True,default=[],verbose_name=_('OperationLocks'))
    InstanceChargeType = models.CharField(max_length=15,verbose_name=_('InstanceChargeType'))
    GPUAmount = models.CharField(max_length=10,verbose_name=_('GPUAmount'))
    LastUpdate = models.DateTimeField(auto_now=True,verbose_name=_('LastUpdat_time'))


    def __unicode__(self):
        return self.hostname

    class Meta:
        ordering = ['ExpiredTime']