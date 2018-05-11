# Generated by Django 2.0 on 2018-04-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180411_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='inneripaddress',
            field=models.CharField(max_length=20, unique=True, verbose_name='InnerIpAddress'),
        ),
        migrations.AlterField(
            model_name='server',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=20, verbose_name='manufacturer'),
        ),
        migrations.AlterField(
            model_name='server',
            name='memory',
            field=models.CharField(blank=True, max_length=20, verbose_name='Memory'),
        ),
        migrations.AlterField(
            model_name='server',
            name='productname',
            field=models.CharField(blank=True, max_length=30, verbose_name='productname'),
        ),
        migrations.AlterField(
            model_name='server',
            name='publicipaddress',
            field=models.CharField(blank=True, max_length=25, verbose_name='PublicIpAddress'),
        ),
        migrations.AlterField(
            model_name='server',
            name='serialnumber',
            field=models.CharField(max_length=50, verbose_name='SerialNumber'),
        ),
    ]