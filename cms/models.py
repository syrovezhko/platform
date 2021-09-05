from django.db import models

# Create your models here.
class CmsSections(models.Model):
    #cms_icon = models.ImageField(upload_to='sctionsimg/', verbose_name='Иконка курса')
    cms_bgColor = models.CharField(max_length=20, verbose_name='Цвет фона карточки (RGB/HEX)', default="#88C3FF")
    cms_сolor = models.CharField(max_length=20, verbose_name='Цвет текста карточки при наведении (RGB/HEX)', default="#000000")
    cms_iconCss = models.CharField(max_length=20, verbose_name='Класс boxicons.com, вместо картинки')
    cms_titleCard = models.CharField(max_length=30, verbose_name='Короткое название кружка', default="-")
    cms_cardItom1 = models.CharField(max_length=200, verbose_name='1 пункт программы обучения', default="")
    cms_cardItom2 = models.CharField(max_length=200, verbose_name='2 пункт программы обучения', default="", blank=True)
    cms_cardItom3 = models.CharField(max_length=200, verbose_name='3 пункт программы обучения', default="", blank=True)
    cms_cardItom4 = models.CharField(max_length=200, verbose_name='4 пункт программы обучения', default="", blank=True)
    cms_cardItom5 = models.CharField(max_length=200, verbose_name='5 пункт программы обучения', default="", blank=True)
    cms_cardItom6 = models.CharField(max_length=200, verbose_name='6 пункт программы обучения', default="", blank=True)
    cms_cardItom7 = models.CharField(max_length=200, verbose_name='7 пункт программы обучения', default="", blank=True)
    cms_cardItom8 = models.CharField(max_length=200, verbose_name='8 пункт программы обучения', default="", blank=True)
    cms_cardItom9 = models.CharField(max_length=200, verbose_name='9 пункт программы обучения', default="", blank=True)
    cms_cardItom10 = models.CharField(max_length=200, verbose_name='10 пункт программы обучения', default="", blank=True)
    cms_level = models.CharField(max_length=2, verbose_name='Уровень сложности программы; от 0, до 9', default="-")
    cms_age = models.CharField(max_length=2, verbose_name='Минимальный возраст учащегося', default="-")
    cms_titleModal = models.CharField(max_length=50, verbose_name='Полное название кружка', default="-")
    cms_termMonths = models.CharField(max_length=2, verbose_name='Срок обучния (мес.)', default="-")
    cms_termTimes = models.CharField(max_length=4, verbose_name='Колличество уроков в программе', default="-")
    cms_regularity = models.CharField(max_length=1, verbose_name='Колличество уроков в неделю', default="-")
    cms_durationH = models.CharField(max_length=2, verbose_name='Продолжительность урока в академических часах', default="-")
    cms_durationM = models.CharField(max_length=3, verbose_name='Продолжительность урока в в минутах', default="-")
    #cms_durationB = models.CharField(max_length=3, verbose_name='Продолжительность перемены в минутах', default="-")
    cms_number = models.CharField(max_length=10, verbose_name='Колличество учащихся в группе (... - ...)', default="-")
    cms_textDesc = models.TextField(max_length=1000, verbose_name='Общая информация', default="-")
    cms_textResult = models.TextField(max_length=1000, verbose_name='Декларируемый результат', default="-")
    cms_payOnce = models.CharField(max_length=5, verbose_name='Одно занятие стоит (не стерайте значек рубля):', default=" ₽")
    cms_payMonthName1 = models.CharField(max_length=20, verbose_name='1 расчетный месяц (просто допишите)', default="Оплата за ")
    cms_payMonth1 = models.CharField(max_length=10, verbose_name='Оплата за 1 расчетный месяц (не стерайте значек рубля)', default=" ₽")
    cms_payMonthName2 = models.CharField(max_length=20, verbose_name='2 расчетный месяц (просто допишите)', default="Оплата за ", blank=True)
    cms_payMonth2 = models.CharField(max_length=10, verbose_name='Оплата за 2 расчетный месяц (не стерайте значек рубля)', default=" ₽", blank=True)
    cms_payMonthName3 = models.CharField(max_length=20, verbose_name='3 расчетный месяц (просто допишите)', default="Оплата за ", blank=True)
    cms_payMonth3 = models.CharField(max_length=10, verbose_name='Оплата за 3 расчетный месяц (не стерайте значек рубля)', default=" ₽", blank=True)
    cms_payMonthName4 = models.CharField(max_length=20, verbose_name='4 расчетный месяц (просто допишите)', default="Оплата за ", blank=True)
    cms_payMonth4 = models.CharField(max_length=10, verbose_name='Оплата 4 расчетный месяц (не стерайте значек рубля)', default=" ₽", blank=True)
    cms_payFull = models.CharField(max_length=20, verbose_name='Полная стоимость обучения (не стерайте значек рубля)', default=" ₽")



    def __str__(self):
        return self.cms_titleCard

    class Meta:
        verbose_name = 'кружок'
        verbose_name_plural = 'кружки'

class TeachersCard(models.Model):
    teachersCard_dt = models.DateTimeField(auto_now=True)
    teachersCard_img = models.ImageField(upload_to='cvimg/', default="/static/img/login.png")
    teachersCard_name = models.CharField(max_length=200, verbose_name='Имя Отчество', default="")
    teachersCard_lname = models.CharField(max_length=200, verbose_name='Фамилия', default="")
    teachersCard_phone = models.CharField(max_length=200, verbose_name="Номер телефона с WhatsApp БЕЗ +7 или 8", default="9852895574")
    teachersCard_tg = models.CharField(max_length=200, verbose_name="Имя пользователя Telegram", default="", blank=True)
    teachersCard_email = models.CharField(max_length=200, verbose_name="Адрес электронной почты", default="")
    teachersCard_degree1 = models.CharField(max_length=200, verbose_name="Высшее образование", default="МАИ, специалист, самолето- и верталетостроение", blank=True)
    teachersCard_degreeYear1 = models.CharField(max_length=200, verbose_name="Год окончания", default="Окончил(а) в 2018г", blank=True)
    #teachersCard_degree2 = models.CharField(max_length=200, verbose_name="Высшее образование", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    #teachersCard_degreeYear2 = models.CharField(max_length=200, verbose_name="Год окончания", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    #teachersCard_degree3 = models.CharField(max_length=200, verbose_name="Высшее образование", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    #teachersCard_degreeYear3 = models.CharField(max_length=200, verbose_name="Год окончания", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    teachersCard_teacherDegree1 = models.CharField(max_length=200, verbose_name="Педагогическое образование", default="Московская академия профессиональных компетенций, проф. переподготовка, информатика в общеобразовательных организациях и организациях профессионального образования", blank=True)
    teachersCard_teacherDegreeYear1 = models.CharField(max_length=200, verbose_name="Год окончания", default="Окончил(а) в 2019г", blank=True)
    teachersCard_teacherDegree2 = models.CharField(max_length=200, verbose_name="Педагогическое образование", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    teachersCard_teacherDegreeYear2 = models.CharField(max_length=200, verbose_name="Год окончания", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    teachersCard_teacherDegree3 = models.CharField(max_length=200, verbose_name="Педагогическое образование", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    teachersCard_teacherDegreeYear3 = models.CharField(max_length=200, verbose_name="Год окончания", default="Второе, третье, магистратура и т.д., при отстутствии стереть", blank=True)
    teachersCard_subject1 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject2 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject3 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject4 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject5 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject6 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject7 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject8 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject9 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject10 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)
    teachersCard_subject11 = models.CharField(max_length=200, verbose_name="Готов преподавать", default="", blank=True)

    def __str__(self):
        return self.teachersCard_name

    class Meta:
        verbose_name = 'педагог'
        verbose_name_plural = 'педагоги'