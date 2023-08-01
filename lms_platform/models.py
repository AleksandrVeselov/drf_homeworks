from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}  # для необязательного поля

PAYMENT_METHOD_CHOICES = [('Cash', 'Наличные'), ('money_transfer', 'денежный перевод')]


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(max_length=255, verbose_name='Название курса')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса')


class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(max_length=255, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    link_to_video = models.CharField(max_length=255, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)  # Ссылка на курс


class Payment(models.Model):
    """Модель платежа"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, verbose_name='Оплаченный курс', on_delete=models.SET_NULL, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='Оплаченный урок', on_delete=models.SET_NULL, **NULLABLE)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Сумма оплаты')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')
