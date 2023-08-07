from rest_framework.pagination import PageNumberPagination

from lms_platform.models import Course, Lesson


class CoursePaginator(PageNumberPagination):
    """Класс-пагинатор для вывода всех курсов на одной странице"""

    page_size = len(Course.objects.all())


class LessonPaginator(PageNumberPagination):
    """Класс-пагинатор для вывода всех уроков на одной странице"""

    page_size = len(Lesson.objects.all())