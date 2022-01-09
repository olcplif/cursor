from rest_framework.viewsets import ModelViewSet

from src.apps.cars.models import Color
from src.apps.cars.serializers.v1.color import ColorSerializer


class ColorModelViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
