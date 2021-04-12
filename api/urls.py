from django.contrib import admin
from django.urls import path, include

from api.api_views.device_view import DeviceListApiView, DeviceDetailsApiView
from api.views import Api
from custom_view.views import Home

urlpatterns = [
    path('',Api.as_view()),
    path('device/',DeviceListApiView.as_view()),
    path('device/<int:id>',DeviceDetailsApiView.as_view())
]
