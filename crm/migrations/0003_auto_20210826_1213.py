# Generated by Django 3.2.6 on 2021-08-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210825_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='enrollment_fname',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='enrollment_lname',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='enrollment_pname',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrollment_name',
            field=models.CharField(default='', max_length=200, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_phone',
            field=models.CharField(default='', max_length=20, verbose_name='Телефон'),
        ),
    ]
