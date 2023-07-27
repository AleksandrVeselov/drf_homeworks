from lms_platform.apps import LmsPlatformConfig
from rest_framework.routers import DefaultRouter

from lms_platform.views import CourseViewSet

app_name = LmsPlatformConfig.name

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [

] + router.urls