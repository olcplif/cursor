import factory

from src.apps.photos.models import Picture


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Picture
