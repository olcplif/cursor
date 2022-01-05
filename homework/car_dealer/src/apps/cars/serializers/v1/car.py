from rest_framework import serializers

from src.apps.cars.models import Car
from src.apps.cars.serializers.v1.color import ColorSerializer
from src.apps.cars.serializers.v1.model import ModelSerializer
from src.apps.cars.serializers.v1.brand import BrandSerializer
from src.apps.cars.serializers.v1.property import PropertySerializer
from src.apps.cars.serializers.v1.car_property import CarPropertySerializer
from src.apps.users.models import CarDealerUsers
from src.apps.users.serializers.v1.user import CarDealerUsersSerializer


class CarSerializer(serializers.Serializer):
    color = ColorSerializer()
    dealer = serializers.PrimaryKeyRelatedField(required=True, queryset=CarDealerUsers.objects.all())
    model = ModelSerializer()
    engine_type = serializers.CharField()
    pollutant_class = serializers.CharField()
    price = serializers.CharField()
    fuel_type = serializers.CharField()
    status = serializers.CharField()
    doors = serializers.CharField()
    capacity = serializers.CharField()
    gear_case = serializers.CharField()
    number = serializers.CharField()
    slug = serializers.CharField()
    sitting_place = serializers.CharField()
    first_registration_data = serializers.DateField(format="%Y-%m-%d")
    engine_power = serializers.CharField()

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data: dict) -> Car:
        instance.color = validated_data.get('color', instance.color)
        instance.dealer = validated_data.get('dealer', instance.dealer)
        instance.model = validated_data.get('model', instance.model)
        instance.engine_type = validated_data.get('engine_type', instance.engine_type)
        instance.pollutant_class = validated_data.get('pollutant_class', instance.pollutant_class)
        instance.price = validated_data.get('price', instance.price)
        instance.fuel_type = validated_data.get('fuel_type', instance.fuel_type)
        instance.status = validated_data.get('status', instance.status)
        instance.doors = validated_data.get('doors', instance.doors)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.gear_case = validated_data.get('gear_case', instance.gear_case)
        instance.number = validated_data.get('number', instance.number)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.sitting_place = validated_data.get('sitting_place', instance.sitting_place)
        instance.first_registration_data = validated_data.get('first_registration_data', instance.first_registration_data)
        instance.engine_power = validated_data.get('engine_power', instance.engine_power)
        instance.save()
        return instance
