from django.apps import AppConfig
from rest_framework.authtoken.admin import TokenAdmin


class UsersConfig(AppConfig):
    name = 'users'


TokenAdmin.raw_id_fields = ['user']
