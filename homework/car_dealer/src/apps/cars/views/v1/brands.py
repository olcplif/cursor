from rest_framework.viewsets import ModelViewSet

from src.apps.cars.models import Brand
from src.apps.cars.serializers.v1.brand import BrandSerializer


class BrandModelViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
