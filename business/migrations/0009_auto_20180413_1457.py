# Generated by Django 2.0 on 2018-04-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20180413_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='createTime',
            field=models.CharField(max_length=120, verbose_name='Create at'),
        ),
    ]