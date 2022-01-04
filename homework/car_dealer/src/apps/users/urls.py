from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from src.apps.users.views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    # path('login/', CustomAuthToken.as_view()),
]

