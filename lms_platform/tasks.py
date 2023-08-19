from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms_platform.models import Subscription, Course


@shared_task
def send_update_email(course: int):
    """Функция отправки письма на почту пользователю при обновлении материалов курса в случае если он на них подписан"""

    subscriptions = Subscription.objects.filter(course=course)
    course = Course.objects.get(id=course)

    if subscriptions:
        for subscription in subscriptions:
            # print('sending....')
            send_mail(subject='Обновление материалов курса',
                      message=f'Материалы курса {course.title} обновлены',
                      recipient_list=[subscription.user.email],
                      from_email=settings.EMAIL_HOST_USER)

    else:
        pass
