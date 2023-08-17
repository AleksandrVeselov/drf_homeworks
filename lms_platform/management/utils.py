import stripe
from config import settings


def get_stripe_link(course) -> str:
    """Функция для получения ссылки на платеж"""

    stripe.api_key = settings.STRIPE_SECRET_KEY  # авторизация на сервере

    product = stripe.Product.create(name=course.title, description=course.description)  # создаем продукт
    # print(product)

    # Создаем цену для продукта
    price = stripe.Price.create(unit_amount_decimal=course.price, currency="rub", product=product.get("id"))
    print(price)

    # Создаем ссылку на платеж
    payment_link = stripe.PaymentLink.create(line_items=[{"price": price.get("id"), "quantity": 1}])
    # print(payment_link)

    return payment_link.get("url")
