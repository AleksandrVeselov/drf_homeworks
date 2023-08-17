from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms_platform.management.utils import get_stripe_link
from lms_platform.models import Course, Lesson, Payment, Subscription
from lms_platform.validators import LinkToVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок"""

    class Meta:
        model = Lesson  # Модель
        fields = '__all__'  # Поля
        validators = [LinkToVideoValidator('link_to_video')]


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс"""

    count_lessons = SerializerMethodField()  # Количество уроков
    lessons = SerializerMethodField()  # список уроков
    is_subscribed = SerializerMethodField()  # Проверка подписки

    def get_count_lessons(self, course):
        """Метод для получения количества уроков в курсе"""

        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        """Метод для получения списка всех уроков в курсе"""

        return [lesson.title for lesson in course.lesson_set.all()]

    def get_is_subscribed(self, course):
        """Метод для проверки подписки к курсу"""

        return Subscription.objects.filter(course=course, user=self.context['request'].user).exists()

    class Meta:
        model = Course  # Модель
        fields = '__all__'  # ПОля


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Платеж"""

    payment_link = SerializerMethodField()  # Ссылка на оплату

    def get_payment_link(self, payment):
        """Метод для получения ссылки на оплату"""
        if payment.course:
            payment_link = get_stripe_link(payment.course)
        else:
            payment_link = get_stripe_link(payment.lesson)
        return payment_link

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписки"""

    class Meta:
        model = Subscription
        fields = '__all__'
