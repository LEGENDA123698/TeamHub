from django.urls import path
import notifications_app.views as views

app_name = 'notifications_app'

urlpatterns = [
    path("", views.NotificationListView.as_view(), name='notifications-list'), 
    path("<int:pk>/", views.NotificationDetailView.as_view(), name='notification-detail'),
    path("create-notification/", views.NotificationCreateView.as_view(), name='create-notification'),
    path("<int:pk>/update-notification/", views.NotificationUpdateView.as_view(), name='update-notification'),
    path("<int:pk>/delete-notification/", views.NotificationDeleteView.as_view(), name='delete-notification'),
]