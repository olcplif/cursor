from rest_framework import serializers

from src.apps.cars.models import Model
from src.apps.cars.serializers.v1.brand import BrandSerializer


class ModelSerializer(serializers.Serializer):
    brand = BrandSerializer()
    name = serializers.CharField(max_length=30)

    def create(self, validated_data: dict) -> Model:
        return Model.objects.create(**validated_data)

    def update(self, instance: Model, validated_data: dict) -> Model:
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
