from django.urls import path

from user import api

urlpatterns = [
    path('verify_phone', api.verify_phone),
    path('register',api.register),
    path('get-profile', api.get_profile),
    path('set-profile', api.set_profile),
    path('upload-avatar', api.upload_avatar),
]