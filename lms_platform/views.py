from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from lms_platform.models import Course, Lesson, Payment, Subscription
from lms_platform.paginators import CoursePaginator, LessonPaginator
from lms_platform.permissions import IsOwnerOrModerator, IsOwner, IsNotModerator
from lms_platform.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from users.models import User
from users.serializiers import UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для модели Курс на основе viewsets"""

    serializer_class = CourseSerializer  # Класс-сериализатор
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """Переопределение метода get_permissions для назначение разных прав доступа на разные дейтсвия"""

        # просматривать список уроков и детальную информацию по ним может любой авторизованный пользователь
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        # создавать курсы может только пользователь, не входящий в группу модераторы
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsNotModerator]

        # редактировать курсы может только создатель курса или модератор
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsOwnerOrModerator]

        # удалять курсы может только их создатель
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]


class LessonCreateApiView(generics.CreateAPIView):
    """Класс-представление для создания урока на основе Generics"""
    serializer_class = LessonSerializer

    # права доступа на добавление урока только для авторизованных пользователей, не входящих в группу модераторы
    # permission_classes = [IsAuthenticated, IsNotModerator]

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()

        # если у урока нет пользователя, то добавляем в базу данные о авторизованном пользователе
        if not new_lesson.owner:
            new_lesson.owner = self.request.user
            new_lesson.save()


class LessonListApiView(generics.ListAPIView):
    """Класс-представление для просмотра списка уроков на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """Класс-представление для просмотра урока на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # permission_classes = [IsAuthenticated]


class LessonUpdateApiView(generics.UpdateAPIView):
    """Класс-представление для изменения урока на основе Generics"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # права доступа на редактирование урока только для его создателя или для пользователей, входящих в группу модераторы
    # permission_classes = [IsAuthenticated, IsOwnerOrModerator]


class LessonDestroyApiView(generics.DestroyAPIView):
    """Класс-представление для удаления уроков на основе Generics"""
    queryset = Lesson.objects.all()

    # permission_classes = [IsAuthenticated, IsOwner]  # права доступа на удаление урока только для его создателя


class PaymentListAPIView(generics.ListAPIView):
    """Класс-представление для вывода списка платежей"""

    serializer_class = PaymentSerializer  # класс-сериализатор
    queryset = Payment.objects.all()  # список платежей
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]  # фильтры

    permission_classes = [IsAuthenticated]

    filterset_fields = ('course', 'lesson', 'payment_method')  # поля по которым можно фильтровать
    ordering_fields = ('payment_date',)  # Поля, по которым можно сортировать
    search_fields = ('course', 'lesson', 'payment_method')  # Поля, по которым можно производить поиск


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Класс-представление для подписки курс на основе Generics"""

    serializer_class = SubscriptionSerializer  # класс-сериализатор
    # permission_classes = [IsAuthenticated]  # права доступа на подписку

    def perform_create(self, serializer, **kwargs):
        """Переопределение метода perform_create для добавления пользователя"""
        new_subscription = serializer.save()  # создаем новую подписку
        if not new_subscription.user:  # если у пользователя
            new_subscription.user = self.request.user  # добавляем пользователя
        new_subscription.course = Course.objects.get(id=self.kwargs['pk'])  # добавляем курс
        new_subscription.save()  # сохраняем новую подписку


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки на курс на основе Generics"""

    queryset = Course.objects.all()  # список уроков

    # permission_classes = [IsAuthenticated]  # права доступа на удаление подписки только для ее создателя

    def perform_destroy(self, instance, **kwargs):
        """Переопределение метода perform_destroy для удаления подписки на курс"""

        # получаем подписку
        subscription = Subscription.objects.get(course_id=self.kwargs['pk'], user=self.request.user)

        subscription.delete()  # удаляем подписку





