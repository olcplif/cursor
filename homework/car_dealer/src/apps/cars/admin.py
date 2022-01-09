from django.contrib import admin

from src.apps.cars.models import *

admin.site.register(Car)
admin.site.register(Property)
admin.site.register(CarProperty)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)



