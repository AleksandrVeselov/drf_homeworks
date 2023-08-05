from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from lms_platform.models import Course, Lesson, Payment
from lms_platform.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.models import User
from users.serializiers import UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для модели Курс на основе viewsets"""

    serializer_class = CourseSerializer  # Класс-сериализатор
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateApiView(generics.CreateAPIView):
    """Класс-представление для создания урока на основе Generics"""
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


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

    serializer_class = PaymentSerializer  # класс-сериализатор
    queryset = Payment.objects.all()  # список платежей
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # фильтры
    filterset_fields = ('course', 'lesson', 'payment_method')  # поля по которым можно фильтровать
    ordering_fields = ('payment_date',)  # Поля, по которым можно сортировать





