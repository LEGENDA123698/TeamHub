from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartView.as_view(), name="main-page"),
    path('search/', views.global_search, name='global_search'),
]