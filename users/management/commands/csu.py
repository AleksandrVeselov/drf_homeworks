from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания суперпользователя"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin@admin.ru',
                                   first_name='admin',
                                   last_name='adov',
                                   phone='12345678',
                                   is_staff=True,
                                   is_superuser=True)

        user.set_password('12356')
        user.save()

