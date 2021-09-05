from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Enrollment(models.Model):
    enrollment_dt = models.DateTimeField(auto_now=True)
    enrollment_name = models.CharField(max_length=200, verbose_name='ФИО заказчика', default="")
    enrollment_kname = models.CharField(max_length=200, verbose_name='Имя учащегося', default="")
    enrollment_age = models.CharField(max_length=2, verbose_name='Возраст учащегося', default="")
    enrollment_phone = models.CharField(max_length=20, verbose_name='Телефон', default="")
    enrollment_section = models.CharField(max_length=100, verbose_name='Кружок', default="")
    enrollment_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')


    def __str__(self):
        return self.enrollment_name

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'запси'

class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'