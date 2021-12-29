from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from src.apps.newsletter.models import NewsLetter


class NewsLetterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    is_active = serializers.BooleanField(required=True)

    def validate_email(self, email_data):
        try:
            email = NewsLetter.objects.get(email=email_data)
            return email
        except
            raise

    def subscribe(self, validated_data: dict) -> NewsLetter:
        return NewsLetter.objects.create(**validated_data)

    def unsubscribe(self, instance: NewsLetter, validated_data: dict) -> NewsLetter:
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance