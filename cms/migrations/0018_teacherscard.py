# Generated by Django 3.2.6 on 2021-08-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20210829_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachersCard_dt', models.DateTimeField(auto_now=True)),
                ('teachersCard_img', models.ImageField(default='/static/img/login.png', upload_to='cvimg/')),
                ('teachersCard_name', models.CharField(default='', max_length=200, verbose_name='Имя Отчество')),
                ('teachersCard_lname', models.CharField(default='', max_length=200, verbose_name='Фамилия')),
                ('teachersCard_phone', models.CharField(default='9852895574', max_length=200, verbose_name='Номер телефона с WhatsApp БЕЗ +7 или 8')),
                ('teachersCard_tg', models.CharField(blank=True, default='', max_length=200, verbose_name='Имя пользователя Telegram')),
                ('teachersCard_email', models.CharField(default='', max_length=200, verbose_name='Адрес электронной почты')),
                ('teachersCard_degree1', models.CharField(blank=True, default='МАИ, специалист, самолето- и верталетостроение', max_length=200, verbose_name='Высшее образование')),
                ('teachersCard_degreeYear1', models.CharField(blank=True, default='Окончил(а) в 2018г', max_length=200, verbose_name='Год окончания')),
                ('teachersCard_teacherDegree1', models.CharField(blank=True, default='Московская академия профессиональных компетенций, проф. переподготовка, информатика в общеобразовательных организациях и организациях профессионального образования', max_length=200, verbose_name='Педагогическое образование')),
                ('teachersCard_teacherDegreeYear1', models.CharField(blank=True, default='Окончил(а) в 2019г', max_length=200, verbose_name='Год окончания')),
                ('teachersCard_teacherDegree2', models.CharField(blank=True, default='Второе, третье, магистратура и т.д., при отстутствии стереть', max_length=200, verbose_name='Педагогическое образование')),
                ('teachersCard_teacherDegreeYear2', models.CharField(blank=True, default='Второе, третье, магистратура и т.д., при отстутствии стереть', max_length=200, verbose_name='Год окончания')),
                ('teachersCard_teacherDegree3', models.CharField(blank=True, default='Второе, третье, магистратура и т.д., при отстутствии стереть', max_length=200, verbose_name='Педагогическое образование')),
                ('teachersCard_teacherDegreeYear3', models.CharField(blank=True, default='Второе, третье, магистратура и т.д., при отстутствии стереть', max_length=200, verbose_name='Год окончания')),
                ('teachersCard_subject1', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject2', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject3', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject4', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject5', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject6', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject7', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject8', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject9', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject10', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
                ('teachersCard_subject11', models.CharField(blank=True, default='', max_length=200, verbose_name='Готов преподавать')),
            ],
            options={
                'verbose_name': 'педагог',
                'verbose_name_plural': 'педагоги',
            },
        ),
    ]
