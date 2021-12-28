from django.contrib import admin

from src.apps.location.models import City, Country

admin.site.register(City)
admin.site.register(Country)
