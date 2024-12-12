from django.urls import path
import notifications_app.views as views

urlpatterns = [
    path("", views.NotificationListView.as_view(), name='notifications-list'), 
    path("<int:pk>/", views.NotificationDetailView.as_view(), name='notification-detail'),
    path("create-notification", views.NotificationCreateView.as_view(), name='create-notification'),
    path("update-notification/<int:pk>/", views.NotificationUpdateView.as_view(), name='update-notification'),
    path("delete-notification/<int:pk>/", views.NotificationDeleteView.as_view(), name='delete-notification'),
]