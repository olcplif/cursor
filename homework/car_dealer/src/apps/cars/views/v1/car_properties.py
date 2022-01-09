from rest_framework.viewsets import ModelViewSet

from src.apps.cars.models import CarProperty
from src.apps.cars.serializers.v1.car_property import CarPropertySerializer


class CarPropertyModelViewSet(ModelViewSet):
    queryset = CarProperty.objects.all()
    serializer_class = CarPropertySerializer
