from django.contrib.auth.models import AbstractUser
from django.db import models

from lms_platform.models import NULLABLE


class User(AbstractUser):
    """модель пользователя с регистрацией по email"""
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=100, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
