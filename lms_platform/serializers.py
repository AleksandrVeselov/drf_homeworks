from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms_platform.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок"""

    class Meta:
        model = Lesson  # Модель
        fields = '__all__'  # Поля


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс"""

    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    # lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        """Метод для получения количества уроков в курсе"""
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        print([el.pk for el in Lesson.objects.filter(course=course)])
        return [el.pk for el in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course  # Модель
        fields = '__all__'  # ПОля
