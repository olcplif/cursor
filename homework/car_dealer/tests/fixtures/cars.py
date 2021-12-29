from uuid import uuid4

import factory

from src.apps.cars.models import Car, Brand, Model
from src.apps.orders.models import Order
# from tests.fixtures.dealers import DealerFactory


class CarBrandFactory(factory.DjangoModelFactory):
    logo = factory.django.ImageField(color='blue')

    class Meta:
        model = Brand


class CarModelFactory(factory.DjangoModelFactory):
    brand = factory.SubFactory(CarBrandFactory)
    name = factory.LazyFunction(lambda: uuid4().hex)

    class Meta:
        model = Model


# class CarFactory(factory.DjangoModelFactory):
#     model = factory.SubFactory(CarModelFactory)
#     dealer = factory.SubFactory(DealerFactory)
#
#     class Meta:
#         model = Car


# class OrderFactory(factory.DjangoModelFactory):
#     car = factory.SubFactory(CarFactory)
#
#     class Meta:
#         model = Order
