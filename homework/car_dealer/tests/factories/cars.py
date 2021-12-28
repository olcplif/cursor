import string

import factory
from factory import fuzzy

from src.apps.cars.models import *
from tests.factories.dealers import CarDealerUsersFactory


class CarBrandFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Brand


class CarModelFactory(factory.django.DjangoModelFactory):
    brand_id = factory.SubFactory(CarBrandFactory)
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Model


class CarColorFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Color


class CarPictureFactory(factory.django.DjangoModelFactory):
    url = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='https://img.com/')
    position = '1'
    metadata = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Picture


class CarPropertyFactory(factory.django.DjangoModelFactory):
    category = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Property


GEAR_CHOICES = [x[0] for x in Car.GEAR_CHOICES]
POLLUTANT_CLASS_CHOICES = [x[0] for x in Car.POLLUTANT_CLASS_CHOICES]
FUEL_CHOICES = [x[0] for x in Car.FUEL_CHOICES]
STATUS_CHOICES = [x[0] for x in Car.STATUS_CHOICES]


class CarFactory(factory.django.DjangoModelFactory):
    color_id = factory.SubFactory(CarColorFactory)
    dealer_id = factory.SubFactory(CarDealerUsersFactory)
    model_id = factory.SubFactory(CarModelFactory)
    engine_type = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    pollutant_class = factory.fuzzy.FuzzyChoice(POLLUTANT_CLASS_CHOICES)
    price = '111'
    fuel_type = factory.fuzzy.FuzzyChoice(FUEL_CHOICES)
    status = factory.fuzzy.FuzzyChoice(STATUS_CHOICES)
    doors = '5'
    capacity = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    gear_case = factory.fuzzy.FuzzyChoice(GEAR_CHOICES)
    number = '10'
    slug = 'test-test'
    sitting_place = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    first_registration_data = factory.Faker('date_object')
    engine_power = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Car


class CarPropertiesFactory(factory.django.DjangoModelFactory):
    property_id = factory.SubFactory(CarPropertyFactory)
    car_id = factory.SubFactory(CarFactory)

    class Meta:
        model = CarProperty
