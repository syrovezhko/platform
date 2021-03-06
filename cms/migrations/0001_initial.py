# Generated by Django 3.2.6 on 2021-08-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_icon', models.ImageField(upload_to='sctionsimg/')),
                ('cms_iconCss', models.CharField(max_length=20, verbose_name='Класс boxicons.com, вместо картинки')),
                ('cms_titleCard', models.CharField(max_length=20, verbose_name='Короткое название кружка')),
                ('cms_cardItom', models.CharField(max_length=50, verbose_name='Пункт программы обучения')),
                ('cms_level', models.CharField(max_length=2, verbose_name='Уровень сложности программы; от 0, до 9')),
                ('cms_titleModal', models.CharField(max_length=50, verbose_name='Полное название кружка')),
                ('cms_termMonths', models.CharField(max_length=2, verbose_name='Срок обучния (мес.)')),
                ('cms_termTimes', models.CharField(max_length=4, verbose_name='Колличество уроков в программе')),
                ('cms_durationH', models.CharField(max_length=2, verbose_name='Продолжительность урока в академических часах')),
                ('cms_durationM', models.CharField(max_length=3, verbose_name='Продолжительность урока в в минутах')),
                ('cms_number', models.CharField(max_length=4, verbose_name='Колличество учащихся в группе')),
                ('cms_textDesc', models.CharField(max_length=200, verbose_name='Общая информация')),
                ('cms_textResult', models.CharField(max_length=100, verbose_name='Декларируемый результат')),
                ('cms_payOnce', models.CharField(max_length=5, verbose_name='Одно занятие стоит:')),
                ('cms_payMonthName', models.CharField(max_length=5, verbose_name='Расчетный месяц')),
                ('cms_payMonth', models.CharField(max_length=5, verbose_name='Оплата за расчетный месяц')),
                ('cms_payFull', models.CharField(max_length=5, verbose_name='Полная стоимость обучения')),
            ],
            options={
                'verbose_name': 'кружок',
                'verbose_name_plural': 'кружки',
            },
        ),
    ]
