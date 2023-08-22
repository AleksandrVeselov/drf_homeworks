from datetime import datetime, timezone, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms_platform.models import Subscription, Course
from celery.utils.log import get_task_logger
from users.models import User

logger = get_task_logger(__name__)


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

@shared_task
def block_user():
    """Функция для блокировки пользователя если он не был в онлайне более месяца"""
    logger.info("function started")
    users = User.objects.all()  # получаем всех пользователей

    for user in users:
        # если пользователь не был в онлайне более месяца, то блокируем его
        if (datetime.now(timezone.utc) - user.last_login) >= timedelta(days=30):
            user.is_active = False
            user.save()
    logger.info("function ended")