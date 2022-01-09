from rest_framework import serializers

from src.apps.cars.models import Brand


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def create(self, validated_data: dict) -> Brand:
        return Brand.objects.create(**validated_data)

    def update(self, instance: Brand, validated_data: dict) -> Brand:
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
