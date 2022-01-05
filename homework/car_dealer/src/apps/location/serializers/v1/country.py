from rest_framework import serializers

from src.apps.location.models import Country


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()

    def create(self, validated_data: dict) -> Country:
        return Country.objects.create(**validated_data)

    def update(self, instance: Country, validated_data: dict) -> Country:
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
