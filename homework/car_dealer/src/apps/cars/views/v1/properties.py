from rest_framework.viewsets import ModelViewSet

from src.apps.cars.models import Property
from src.apps.cars.serializers.v1.property import PropertySerializer


class PropertyModelViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
