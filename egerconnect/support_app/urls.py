# support/urls.py

from django.urls import path
from .views import create_message

urlpatterns = [
    path("messages/", create_message),
]
