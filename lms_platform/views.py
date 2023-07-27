from rest_framework import viewsets

from lms_platform.models import Course
from lms_platform.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
