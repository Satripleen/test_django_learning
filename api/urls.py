from django.contrib import admin
from django.urls import path, include

from api.api_views.customer_view import CustomerListApiView, CustomerDetailsApiView
from api.api_views.device_view import DeviceListApiView, DeviceDetailsApiView
from api.api_views.history_view import HistoryListApiView
from api.views import Api
from custom_view.views import Home

urlpatterns = [
    path('',Api.as_view()),
    path('device/',DeviceListApiView.as_view()),
    path('device/<int:id>',DeviceDetailsApiView.as_view()),
    path('customer/',CustomerListApiView.as_view()),
    path('customer/<int>:id',CustomerDetailsApiView.as_view),
    path('history/',HistoryListApiView.as_view())
]
