from django.urls import path

from lms_platform.apps import LmsPlatformConfig
from rest_framework.routers import DefaultRouter

from lms_platform.views import CourseViewSet, LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, \
    LessonUpdateApiView, LessonDestroyApiView, PaymentListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView, PaymentCreateAPIView

app_name = LmsPlatformConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/', LessonListApiView.as_view(), name='lesson'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyApiView.as_view(), name='lesson_delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment'),
    path('course/<int:pk>/subscribe/', SubscriptionCreateAPIView.as_view(), name='subscribe'),
    path('course/<int:pk>/unsubscribe/', SubscriptionDestroyAPIView.as_view(), name='unsubscribe'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
] + router.urls
