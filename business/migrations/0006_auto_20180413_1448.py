# Generated by Django 2.0 on 2018-04-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20180413_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='Service ID'),
        ),
    ]
