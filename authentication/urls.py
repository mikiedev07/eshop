from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
