from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.StartView.as_view(), name = "main-page"),
    path('ezvenenya/', views.EzvenenyaView.as_view(), name = "ezvenenya"),
]