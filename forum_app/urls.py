from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'forum_app'


urlpatterns = [
    path('', SectionListView.as_view(), name="forum-start"),
    path('section/<int:pk>/', SectionDetailView.as_view(), name='section_detail'),
    path('theme/<int:pk>/', ThemeDetailView.as_view(), name='theme_detail'),
    path('section/create/', SectionCreateView.as_view(), name='section-create'),

]