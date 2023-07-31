from django.db import models

NULLABLE = {'null': True, 'blank': True}  # для необязательного поля


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
