from django.contrib import admin

# Register your models here.
from src.apps.newsletter.models import *


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = ('email',)
# admin.site.register(NewsLetter)
