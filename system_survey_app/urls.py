from django.urls import path
from .views import *


urlpatterns = [
    path('', SurveyListView.as_view(), name='list-surveys'),
    path('surveys/<int:pk>/', SurveyDetailView.as_view(), name='detail-survey'),
    path('surveys/<int:pk>/add-question/', AddQuestionView.as_view(), name='add-question'),
    path('users/', UserListView.as_view(), name='list-users'),
    path('users/<int:user_id>/surveys/', UserListSurveyView.as_view(), name='user-list-surveys'),
    path('users/<int:pk>/survey-details/<int:user_id>', UserDetailSurveyView.as_view(), name='user-detail-survey'),
    path('add-survey/', AddSurveyView.as_view(), name='add-survey'),
    path('surveys/<int:survey_pk>/questions/<int:pk>/edit/', UpdateQuestionView.as_view(), name='edit-question'),
    path('surveys/<int:survey_pk>/questions/<int:pk>/delete/', DeleteQuestionView.as_view(), name='delete-question'),
    path('surveys/<int:pk>/delete/', DeleteSurveyView.as_view(), name='delete-survey'),

]