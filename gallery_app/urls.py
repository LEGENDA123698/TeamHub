from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', GalleryStartView.as_view(), name='gallery-start'),
    path('create/', ImageCreateView.as_view(), name='image-create'),
    path('update/<int:pk>/', ImageUpdateView.as_view(), name='image-update'),
    path('delete/<int:pk>/', ImageDeleteView.as_view(), name='image-delete'),
]