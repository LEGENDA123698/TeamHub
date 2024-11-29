from django.urls import path
from auth_app import views

urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name = "register"),
]