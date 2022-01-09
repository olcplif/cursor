import string

import factory
from factory import fuzzy

from src.apps.pictures.models import *
from tests.factories.cars import CarFactory


class CarPictureFactory(factory.django.DjangoModelFactory):
    car_id = factory.SubFactory(CarFactory)
    url = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    position = '1'
    metadata = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Picture
