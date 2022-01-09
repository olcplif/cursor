from rest_framework import generics

from src.apps.cars.models import Car
from src.apps.cars.serializers.v1.car import CarSerializer


class CarsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.active()
    serializer_class = CarSerializer
