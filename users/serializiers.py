from datetime import datetime, timezone, timedelta

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms_platform.tasks import block_user
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователь"""

    # # для теста функции block_user()
    # time_from_last_login = SerializerMethodField()
    # def get_time_from_last_login(self, user):
    #     block_user()
    #     return (datetime.now(timezone.utc) - user.last_login) >= timedelta(days=30)

    class Meta:
        model = User  # Модель
        fields = '__all__'  # ПОля

    def save(self, **kwargs):
        """Сохранение пользователя в базу данных"""

        data = super().save(**kwargs)
        data.set_password(self.validated_data['password'])  # Задание пароля
        data.save()  # Сохранение в базе данных

        return data
