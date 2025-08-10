from django.urls import path
from .views import UserRegister
from rest_framework.authtoken import views

urlpatterns = [
    path('register', UserRegister.as_view(), name='user_register'),
    path('login', views.obtain_auth_token),
]