from django.urls import path
import calendar_app.views as views


urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_with_date'), # просмотр календаря
    path("create_event/", views.EventCreateView.as_view(), name="create_event"), # создание события
    path("update_event/<int:pk>/", views.EventUpdateView.as_view(), name="update_event"), # обновление события
    path("delete_event/<int:pk>/", views.EventDeleteView.as_view(), name="delete_event"), # удаление события
]
