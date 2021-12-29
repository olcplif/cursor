from django.urls import path, include
from src.apps.newsletter.views import NewsLetterView, success_view

app_name = 'newsletter'

urlpatterns = [
    path('subscribe/add', NewsLetterView.as_view(), name='new-subscribe'),
    path('subscribe/success', success_view, name='success-subscribe'),
]