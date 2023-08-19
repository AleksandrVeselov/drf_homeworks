import stripe
from config import settings
from lms_platform.models import Course


def get_stripe_link(payment) -> str:
    """Функция для получения ссылки на платеж"""

    stripe.api_key = settings.STRIPE_SECRET_KEY  # авторизация на сервере

    # если у платежа есть курс, получаем курс. Иначе получаем урок.
    if payment.course:
        purchase = payment.course  # получаем курс
    else:
        purchase = payment.lesson   # получаем урок

    product = stripe.Product.create(name=purchase.title, description=purchase.description)  # создаем продукт
    # print(product)

    # Создаем цену для продукта (stripe считает что цена в копейках или центах.
    # Умножаем на 100 чтобы получить доллары или рубли)
    price = stripe.Price.create(unit_amount_decimal=purchase.price * 100,
                                currency=purchase.currency,
                                product=product.get("id"))

    # Создаем ссылку на платеж
    payment_link = stripe.PaymentLink.create(line_items=[{"price": price.get("id"), "quantity": 1}],
                                             after_completion={'redirect':
                                                                   {'url': f'http://127.0.0.1:8000/confirm_payment'
                                                                           f'/{payment.pk}/'},
                                                               'type': 'redirect'})
    # print(payment_link)

    return payment_link.get("url")
