import re
from collections import OrderedDict

from rest_framework.exceptions import ValidationError


class LinkToVideoValidator:
    """Класс-валидатор ссылки на видео.
    Проверяет отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value: OrderedDict) -> None:

        pattern = r'https://www.youtube.com/.*'  # Шаблон ссылки на видео.
        tmp_val = dict(value).get(self.field)  # Получаем значение поля ссылки из словаря.

        # Если в ссылке не находится совпадений с шаблоном, генерируется исключение
        if not bool(re.search(pattern, tmp_val)):
            raise ValidationError('Ссылка не должна вести на сторонние ресурсы, кроме youtube.com.')

