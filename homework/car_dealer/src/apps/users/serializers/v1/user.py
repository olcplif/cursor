from rest_framework import serializers

from src.apps.users.models import CarDealerUsers
from src.apps.location.serializers.v1.city import CitySerializer


class CarDealerUsersSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    is_dealer = serializers.BooleanField(default=False, required=False)
    is_client = serializers.BooleanField(default=False, required=False)
    city_id = CitySerializer()
    full_name = serializers.SerializerMethodField(method_name='user_fullname')

    def user_fullname(self, instance: CarDealerUsers) -> str:
        return instance.get_full_name()

    class Meta:
        model = CarDealerUsers
        fields = ('username', 'full_name', 'id', 'avatar', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }
