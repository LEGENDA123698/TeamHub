from django.urls import path
import materials_app.views as views


urlpatterns = [
    path('materials/', views.materials_view, name='materials'),
    path('materials/add_material', views.MaterialAddView.as_view(), name='add_material'),
    path("materials/update_material/<str:value>/<int:pk>/", views.MaterialUpdateView.as_view(), name="update_material"),
    path("materials/delete_material/<str:value>/<int:pk>/", views.MaterialDeleteView.as_view(), name="delete_material"),
]