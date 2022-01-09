import string

import factory
from factory import fuzzy

from src.apps.location.models import City, Country


class CountryFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    code = fuzzy.FuzzyText(length=7, chars=string.ascii_letters, prefix='')

    class Meta:
        model = Country


class CityFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    country_id = factory.SubFactory(CountryFactory)

    class Meta:
        model = City
