# Generated by Django 2.0.7 on 2018-11-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='capacity',
            field=models.CharField(max_length=64, verbose_name='磁盘容量GB'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='model',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘型号'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='pd_type',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘类型'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='capacity',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='容量'),
        ),
    ]
