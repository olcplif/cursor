from rest_framework import serializers

from src.apps.location.models import City
from src.apps.location.serializers.v1.country import CountrySerializer


class CitySerializer(serializers.Serializer):
    name = serializers.CharField()
    country_id = CountrySerializer()

    def create(self, validated_data: dict) -> City:
        return City.objects.create(**validated_data)

    def update(self, instance: City, validated_data: dict) -> City:
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
