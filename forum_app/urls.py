from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', SectionListView.as_view(), name="forum-start")
]