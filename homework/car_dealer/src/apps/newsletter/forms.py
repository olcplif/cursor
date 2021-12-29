from django import forms
from django.forms import ModelForm
from src.apps.newsletter.models import NewsLetter


class NewsLetterModelForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
