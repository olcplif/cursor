import string

import factory
from factory import fuzzy

from src.apps.newsletter.models import NewsLetter


class NewsLetterFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())

    class Meta:
        model = NewsLetter
