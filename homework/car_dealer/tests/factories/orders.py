import string

import factory
from factory import fuzzy

from src.apps.orders.models import Order
from tests.factories.cars import CarFactory

STATUS_CHOICES = [x[0] for x in Order.STATUS_CHOICES]


class OrderFactory(factory.django.DjangoModelFactory):
    car_id = factory.SubFactory(CarFactory)
    status = factory.fuzzy.FuzzyChoice(STATUS_CHOICES)
    first_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    last_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())
    phone = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='+380')
    message = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Order
