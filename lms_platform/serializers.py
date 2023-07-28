from rest_framework import serializers

from lms_platform.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс"""
    class Meta:
        model = Course  # Модель
        fields = '__all__'  # ПОля


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок"""
    class Meta:
        model = Lesson  # Модель
        fields = '__all__'  # Поля

