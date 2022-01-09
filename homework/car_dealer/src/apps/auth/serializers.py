from rest_framework import serializers
# from django.contrib.auth.models import User
from src.apps.users.models import CarDealerUsers


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        model = CarDealerUsers
        fields = ('user_id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        model = CarDealerUsers
        fields = ('user_id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CarDealerUsers.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
