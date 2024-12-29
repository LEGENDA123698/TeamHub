from django.urls import path
import calendar_app.views as views

app_name = 'calendar_app'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_with_date'), # просмотр календаря
    path("create_event/", views.EventCreateView.as_view(), name="calendar_create_event"), # создание события
    path("update_event/<int:pk>/", views.EventUpdateView.as_view(), name="calendar_update_event"), # обновление события
    path("delete_event/<int:pk>/", views.EventDeleteView.as_view(), name="calendar_delete_event"), # удаление события
]
