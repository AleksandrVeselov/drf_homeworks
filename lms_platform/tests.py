from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms_platform.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тестирование уроков"""

    def setUp(self):
        self.user = User.objects.create(email='test_user@test,ru', password='test_password', phone='test_phone')
        self.course = Course.objects.create(title='Тестовый курс', description='Описание тестового курса',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(title='Урок 25.2', description='Описание урока 25.2',
                                            link_to_video='https://www.youtube.com/', owner=self.user,
                                            course=self.course)

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {
            'title': 'Урок 25.2 другой',
            "description": "Описание урока 25.2 другое",
            'link_to_video': 'https://www.youtube.com/',
            'owner': self.user.pk,
        }

        response = self.client.post(reverse('lms_platform:lesson_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        self.assertEqual(Lesson.objects.all().count(), 2)  # Проверка наличия в базе данных новой записи

    def test_list_lessons(self):
        """Тестирование списка уроков"""

        response = self.client.get(reverse('lms_platform:lesson'))  # Запрос на получение списка уроков

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         [{'id': self.lesson.pk,
                           'title': self.lesson.title,
                           'description': self.lesson.description,
                           'preview': None,
                           'link_to_video': self.lesson.link_to_video,
                           'course': self.course.pk,
                           'owner': self.user.pk}]
                         )

    def test_update_lessons(self):
        """Тестирование обновления урока"""

        data = {
            'title': 'Урок 25.2 измененный',
            "description": "Описание урока 25.2 измененное",
            'preview': '',
            'link_to_video': 'https://www.youtube.com/',
            'course': self.course.pk,
            'owner': self.user.pk
        }

        response = self.client.put(reverse('lms_platform:lesson_update', args=[self.lesson.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {'id': self.lesson.pk,
                          'title': "Урок 25.2 измененный",
                          'description': 'Описание урока 25.2 измененное',
                          'preview': None,
                          'link_to_video': self.lesson.link_to_video,
                          'course': self.course.pk,
                          'owner': self.user.pk}
                         )

    def test_get_lessons_by_id(self):
        """Тестирование получения урока по id"""

        response = self.client.get(reverse('lms_platform:lesson_get', args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {'id': self.lesson.pk,
                          'title': self.lesson.title,
                          'description': self.lesson.description,
                          'preview': None,
                          'link_to_video': self.lesson.link_to_video,
                          'course': self.course.pk,
                          'owner': self.user.pk}
                         )

    def test_destroy_lessons(self):
        """Тестирование удаления урока"""

        response = self.client.delete(reverse('lms_platform:lesson_delete', args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

    def test_subscribe_unsubscribe_course(self):
        """Тестирование подписки на урок"""

        data = {
            'user': self.user.pk,
        }

        response = self.client.post(reverse('lms_platform:subscribe', args=[self.course.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        # Проверка наличия подписки на курс
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)

        response = self.client.delete(reverse('lms_platform:unsubscribe', args=[self.course.pk]))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        # Проверка отсутствия подписки на курс
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)
