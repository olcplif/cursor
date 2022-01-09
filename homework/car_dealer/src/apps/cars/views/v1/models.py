from rest_framework.viewsets import ModelViewSet

from src.apps.cars.models import Model
from src.apps.cars.serializers.v1.model import ModelSerializer


class ModelModelViewSet(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
