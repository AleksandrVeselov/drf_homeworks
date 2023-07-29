from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователь"""
    class Meta:
        model = User  # Модель
        fields = '__all__'  # ПОля