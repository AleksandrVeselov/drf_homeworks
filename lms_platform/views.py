from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from lms_platform.models import Course, Lesson, Payment
from lms_platform.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.models import User
from users.serializiers import UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для модели Курс на основе viewsets"""

    serializer_class = CourseSerializer  # Класс-сериализатор
    queryset = Course.objects.all()


class LessonCreateApiView(generics.CreateAPIView):
    """Класс-представление для создания урока на основе Generics"""
    serializer_class = LessonSerializer


class LessonListApiView(generics.ListAPIView):
    """Класс-представление для просмотра списка уроков на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """Класс-представление для просмотра урока на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateApiView(generics.UpdateAPIView):
    """Класс-представление для изменения урока на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyApiView(generics.DestroyAPIView):
    """Класс-представление для удаления уроков на основе Generics"""
    queryset = Lesson.objects.all()


class UserCreateApiView(generics.CreateAPIView):
    """Класс-представление для создания пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    """Класс-представление для вывода списка платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('course', 'lesson', 'payment_method')





