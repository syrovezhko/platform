# Generated by Django 3.2.6 on 2021-08-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20210828_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmssections',
            name='cms_payFull',
            field=models.CharField(max_length=20, verbose_name='Полная стоимость обучения'),
        ),
        migrations.AlterField(
            model_name='cmssections',
            name='cms_payMonth',
            field=models.CharField(max_length=10, verbose_name='Оплата за расчетный месяц'),
        ),
        migrations.AlterField(
            model_name='cmssections',
            name='cms_payMonthName',
            field=models.CharField(max_length=20, verbose_name='Расчетный месяц'),
        ),
    ]
