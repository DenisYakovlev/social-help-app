from django.urls import path
from .views import UserAuth

urlpatterns = [
    path('auth', UserAuth.as_view()),
]