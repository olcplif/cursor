from rest_framework import serializers

from src.apps.cars.models import Property


class PropertySerializer(serializers.Serializer):
    category = serializers.CharField()
    name = serializers.CharField()

    def create(self, validated_data: dict) -> Property:
        return Property.objects.create(**validated_data)

    def update(self, instance: Property, validated_data: dict) -> Property:
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
