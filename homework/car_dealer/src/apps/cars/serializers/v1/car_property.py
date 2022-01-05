from rest_framework import serializers

from src.apps.cars.models import Property
from src.apps.cars.models import Car
from src.apps.cars.serializers.v1.property import PropertySerializer
from src.apps.cars.serializers.v1.car import CarSerializer


class CarPropertySerializer(serializers.Serializer):
    property = PropertySerializer(many=True)
    car = PropertySerializer(many=True)

    def create(self, validated_data: dict) -> Property:
        return Property.objects.create(**validated_data)

    def update(self, instance: Property, validated_data: dict) -> Property:
        instance.property = validated_data.get('property', instance.property)
        instance.car = validated_data.get('car', instance.car)
        instance.save()
        return instance
