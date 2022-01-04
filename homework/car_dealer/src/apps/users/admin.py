from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from src.apps.users.models import CarDealerUsers


class CarDealerUsersAdmin(admin.ModelAdmin):
    readonly_fields = ('user_id',)


admin.site.register(CarDealerUsers, CarDealerUsersAdmin)
# admin.site.register(CarDealerUsers)
TokenAdmin.raw_id_fields = ['user']
