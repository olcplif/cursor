import factory
from factory import fuzzy

# from src.apps.users.models import CarDealerUsers, City
from src.apps.location.models import City, Country


class CountryFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Country


class CityFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = City
