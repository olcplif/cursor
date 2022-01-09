from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.cars.api_views import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView
from src.apps.cars.views.v1.cars import CarsListCreateAPIView
from src.apps.cars.views.v1.brands import BrandModelViewSet
from src.apps.cars.views.v1.car_properties import CarPropertyModelViewSet
from src.apps.cars.views.v1.colors import ColorModelViewSet
from src.apps.cars.views.v1.models import ModelModelViewSet
from src.apps.cars.views.v1.properties import PropertyModelViewSet

app_name = 'car'

router = DefaultRouter()
router.register('brands', BrandModelViewSet)
router.register('models', ModelModelViewSet)
router.register('colors', ColorModelViewSet)
router.register('property', PropertyModelViewSet)
router.register('car_properties', CarPropertyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:car_id>', CarRetrieveUpdateDestroyAPIView.as_view(), name='car-detail'),
]
