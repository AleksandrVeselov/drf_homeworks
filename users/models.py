from django.contrib.auth.models import AbstractUser
from django.db import models

from lms_platform.models import NULLABLE


class User(AbstractUser):
    """модель пользователя с регистрацией по email"""
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=100, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Город')
    avatar = models.ImageField(verbose_name='Аватар', **NULLABLE)
