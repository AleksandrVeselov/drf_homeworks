from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms_platform.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс"""

    count_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        """Метод для получения количества уроков в курсе"""
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course  # Модель
        fields = '__all__'  # ПОля


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок"""
    class Meta:
        model = Lesson  # Модель
        fields = '__all__'  # Поля

