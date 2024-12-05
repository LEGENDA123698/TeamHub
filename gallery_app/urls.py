from django.urls import path
from trelloapp import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create_task', views.TaskCreateView.as_view(), name='create_task'),
    path('task_detail/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('update_task/<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),
    path('register', views.RegistrationView.as_view(), name='register')
]