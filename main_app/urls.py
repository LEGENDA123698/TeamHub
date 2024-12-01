from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('', StartView.as_view(), name="start"),