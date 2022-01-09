from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.cars.models import Car
from src.apps.cars.permissions import IsDealerOrReadOnly
from src.apps.cars.serializers.v1.car import CarSerializer


class CarAPIView(APIView):
    permission_classes = (IsDealerOrReadOnly,)

    def get_object(self, pk: int):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, car_id: int) -> Response:
        car = self.get_object(car_id)
        serializer = CarSerializer(instance=car)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self):
        serializer = CarSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # TODO check if serializer data has been updated
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, car_id: int):
        car = self.get_object(car_id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _perform_update(self, car, data, partial=False):
        serializer = CarSerializer(instance=car, data=self.request.data, partial=partial)
        serializer.save()
        return serializer.data

    def put(self, car_id: int):
        car = self.get_object(car_id)
        data = self._perform_update(car, self.request.data)
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, car_id: int):
        car = self.get_object(car_id)
        data = self._perform_update(car, self.request.data, partial=True)
        return Response(data=data, status=status.HTTP_200_OK)


class CarListCreateAPIView(generics.ListCreateAPIView):
    # POST/GET list
    # /cars
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsDealerOrReadOnly,)


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # GET/ PUT / PATCH / DELETE
    # /cars/{id}
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_url_kwarg = 'car_id'
    permission_classes = (IsDealerOrReadOnly,)

    def get_queryset(self):
        return self.queryset.select_related('dealer')
