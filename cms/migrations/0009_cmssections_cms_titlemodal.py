# Generated by Django 3.2.6 on 2021-08-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20210829_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmssections',
            name='cms_titleModal',
            field=models.CharField(default='', max_length=50, verbose_name='Полное название кружка'),
        ),
    ]
