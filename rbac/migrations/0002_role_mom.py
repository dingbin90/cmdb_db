# Generated by Django 2.0.7 on 2018-11-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='mom',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
    ]