from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'forum_app'

urlpatterns = [
    path('', SectionListView.as_view(), name="forum-start"),
    path('section/<int:pk>/', SectionDetailView.as_view(), name='section_detail'),
    path('theme/<int:pk>/', ThemeDetailView.as_view(), name='theme_detail'),
    path('section/create/', SectionCreateView.as_view(), name='section-create'),
    path('section/<int:section_pk>/theme/create/', ThemeCreateView.as_view(), name='theme-create'),
    path('section/<int:pk>/delete/', SectionDeleteView.as_view(), name='section-delete'),
    path('section/<int:pk>/update/', SectionUpdateView.as_view(), name='section-update'),
    path('theme/<int:pk>/delete/', ThemeDeleteView.as_view(), name='theme-delete'),
    path('theme/<int:pk>/update/', ThemeUpdateView.as_view(), name='theme-update'),
]
