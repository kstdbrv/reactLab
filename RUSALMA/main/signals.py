from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import *


def order_created(sender, instance, created, **kwargs):
    if created:
        data = """ 
            У вас новая заявка от {0}
            --------------------------
            Номер телефона: {1}
            Email: {2}
            Категории: {3}, {4}
        """.format(instance.name.capitalize(),  instance.phone, instance.email, instance.category, instance.subcategory)
        send_mail(
            'Новая заявка!',
            data,
            'reactlab.pro@yandex.ru',
            ['web@reactlab.pro']
        )


post_save.connect(order_created, sender=Order)



