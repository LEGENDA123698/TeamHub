from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', StartView.as_view(), name="start"),
]