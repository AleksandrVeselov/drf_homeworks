from django.core.management import BaseCommand


class Command(BaseCommand):
    """Комманда для заполнения базы данных"""

    def handle(self, *args, **kwargs):

        payments_list = [
            {}
        ]