from rest_framework import serializers

from src.apps.cars.models import Color


class ColorSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data: dict) -> Color:
        return Color.objects.create(**validated_data)

    def update(self, instance: Color, validated_data: dict) -> Color:
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
