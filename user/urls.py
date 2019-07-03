from django.urls import path

from user import api

urlpatterns = [
    path('verify_phone', api.verify_phone),
    path('register',api.register),
]