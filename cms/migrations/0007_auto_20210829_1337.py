# Generated by Django 3.2.6 on 2021-08-29 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20210829_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmssections',
            name='cms_age',
        ),
        migrations.RemoveField(
            model_name='cmssections',
            name='cms_level',
        ),
        migrations.RemoveField(
            model_name='cmssections',
            name='cms_titleCard',
        ),
    ]