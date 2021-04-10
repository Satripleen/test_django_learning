from django.contrib import admin
from django.urls import path, include

from api.views import Api
from custom_view.views import Home

urlpatterns = [
    path('',Api.as_view()),
]
