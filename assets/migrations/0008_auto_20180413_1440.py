# Generated by Django 2.0 on 2018-04-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20180411_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='inneripaddress',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='InnerIpAddress'),
        ),
    ]
