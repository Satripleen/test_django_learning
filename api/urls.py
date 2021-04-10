from django.contrib import admin
from django.urls import path, include

from api.api_views.device_view import DeviceApiView
from api.views import Api
from custom_view.views import Home

urlpatterns = [
    path('',Api.as_view()),
    path('device/',DeviceApiView.as_view())
]
