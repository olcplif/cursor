import string

import factory
from factory import fuzzy

from src.apps.users.models import CarDealerUsers
from tests.factories.locations import CityFactory


class CarDealerUsersFactory(factory.django.DjangoModelFactory):
    first_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    last_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    username = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    title = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())
    city_id = factory.SubFactory(CityFactory)

    class Meta:
        model = CarDealerUsers
