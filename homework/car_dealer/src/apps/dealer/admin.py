from django.contrib import admin

from src.apps.dealer.models import *
# Register your models here.
admin.site.register(Dealer)
admin.site.register(City)
admin.site.register(Country)
