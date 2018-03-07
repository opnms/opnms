# Generated by Django 2.0 on 2018-03-07 01:02

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloudprovider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='IDC Name')),
                ('keyid', models.CharField(max_length=50, verbose_name='Key ID')),
                ('keysecret', models.CharField(max_length=50, verbose_name='Secret')),
                ('abbr_name', models.SlugField(blank=True, max_length=15, null=True, unique=True, verbose_name='Abbr Slug')),
                ('country', models.CharField(default='CN', max_length=5, verbose_name='Country')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('create_by', models.CharField(max_length=100, verbose_name='Create by')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstanceType', models.CharField(blank=True, max_length=50, verbose_name='InstanceType')),
                ('InstanceId', models.CharField(max_length=50, verbose_name='InstanceID')),
                ('SerialNumber', models.CharField(max_length=50, unique=True, verbose_name='SerialNumber')),
                ('ImageId', models.CharField(max_length=70, verbose_name='Image ID')),
                ('InstanceTypeFamily', models.CharField(max_length=50, verbose_name='InstanceTypeFamily')),
                ('VlanId', models.CharField(blank=True, max_length=50, verbose_name='VlanId')),
                ('InternetMaxBandwidthIn', models.CharField(max_length=10, verbose_name='InternetMaxBandwidthIn')),
                ('ZoneId', models.CharField(blank=True, max_length=15, verbose_name='Zone')),
                ('InternetChargeType', models.CharField(max_length=50, verbose_name='InternetChargeType')),
                ('SpotStrategy', models.CharField(max_length=50, verbose_name='SpotStrategy')),
                ('StoppedMode', models.CharField(max_length=50, verbose_name='StoppedMode')),
                ('IoOptimized', models.BooleanField(verbose_name='IoOptimized')),
                ('Memory', models.CharField(max_length=50, verbose_name='Memory')),
                ('Cpu', models.CharField(max_length=10, verbose_name='Cpu')),
                ('DeviceAvailable', models.BooleanField(max_length=50, verbose_name='DeviceAvailable')),
                ('SaleCycle', models.CharField(blank=True, max_length=50, verbose_name='SaleCycle')),
                ('SpotPriceLimit', models.CharField(max_length=20, verbose_name='SpotPriceLimit')),
                ('AutoReleaseTime', models.CharField(blank=True, max_length=50, verbose_name='AutoReleaseTime')),
                ('StartTime', models.CharField(max_length=50, verbose_name='StartTime')),
                ('InstanceName', models.CharField(max_length=100, verbose_name='InstanceName')),
                ('Description', jsonfield.fields.JSONField(blank=True, max_length=50, verbose_name='Description')),
                ('ResourceGroupId', models.CharField(blank=True, max_length=50, verbose_name='ResourceGroupId')),
                ('OSType', models.CharField(max_length=25, verbose_name='OSType')),
                ('OSName', models.CharField(max_length=50, verbose_name='OSName')),
                ('InstanceNetworkType', models.CharField(max_length=25, verbose_name='InstanceNetworkType')),
                ('HostName', models.CharField(max_length=50, verbose_name='HostName')),
                ('CreationTime', models.CharField(max_length=50, verbose_name='CreationTime')),
                ('Status', models.CharField(max_length=15, verbose_name='Status')),
                ('ClusterId', models.CharField(blank=True, max_length=50, verbose_name='ClusterId')),
                ('GPUSpec', models.CharField(blank=True, max_length=25, verbose_name='GPUSpec')),
                ('InnerIpAddress', jsonfield.fields.JSONField(blank=True, verbose_name='InnerIpAddress')),
                ('PublicIpAddress', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='PublicIpAddress')),
                ('SecurityGroupIds', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='SecurityGroupIds')),
                ('ExpiredTime', models.CharField(max_length=50, verbose_name='ExpiredTime')),
                ('EipAddress', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='EipAddress')),
                ('VpcAttributes', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='VpcAttributes')),
                ('InternetMaxBandwidthOut', models.CharField(max_length=15, verbose_name='InternetMaxBandwidthOut')),
                ('Recyclable', models.BooleanField(verbose_name='Recyclable')),
                ('RegionId', models.CharField(max_length=25, verbose_name='RegionId')),
                ('OperationLocks', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='OperationLocks')),
                ('InstanceChargeType', models.CharField(max_length=15, verbose_name='InstanceChargeType')),
                ('GPUAmount', models.CharField(max_length=10, verbose_name='GPUAmount')),
                ('LastUpdate', models.DateTimeField(auto_now=True, verbose_name='LastUpdat_time')),
            ],
            options={
                'ordering': ['ExpiredTime'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Region')),
                ('city', models.CharField(max_length=15, unique=True, verbose_name='City')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('create_by', models.CharField(max_length=100, verbose_name='Create by')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Cloudprovider', verbose_name='Cloud Provider')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='HostName')),
                ('inneripaddress', models.CharField(max_length=20, verbose_name='InnerIpAddress')),
                ('publicipaddress', models.CharField(max_length=25, verbose_name='PublicIpAddress')),
                ('serialnumber', models.CharField(max_length=50, unique=True, verbose_name='SerialNumber')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='manufacturer')),
                ('productname', models.CharField(max_length=30, verbose_name='productname')),
                ('esc', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='esc')),
                ('os', models.CharField(blank=True, max_length=25, null=True, verbose_name='os')),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='purchase_date')),
                ('maintain', models.BooleanField(default=False, verbose_name='maintain')),
                ('cpu_model', models.CharField(blank=True, max_length=100, verbose_name='cpu_model')),
                ('cpu_nums', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='cpu_nums')),
                ('memory', models.CharField(max_length=20, verbose_name='Memory')),
                ('hd', models.TextField(blank=True, verbose_name='hd')),
                ('nic', models.TextField(blank=True, verbose_name='nic')),
                ('virtual', models.CharField(blank=True, max_length=20, verbose_name='virtual')),
                ('kernel', models.CharField(blank=True, max_length=200, verbose_name='kernel')),
                ('shell', models.CharField(blank=True, max_length=10, verbose_name='shell')),
                ('saltversion', models.CharField(blank=True, max_length=10, verbose_name='saltversion')),
                ('locale', models.CharField(blank=True, max_length=200, verbose_name='locale')),
                ('selinux', models.CharField(blank=True, max_length=50, verbose_name='selinux')),
                ('lastupdate', models.DateTimeField(auto_now=True, verbose_name='LastUpdat_time')),
                ('create_by', models.CharField(max_length=50, verbose_name='Create by')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('minion', models.ForeignKey(on_delete=True, to='deploy.SaltHost', verbose_name='Salt Minion')),
            ],
            options={
                'ordering': ['hostname'],
            },
        ),
    ]
