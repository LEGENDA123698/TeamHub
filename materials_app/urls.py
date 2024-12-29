from django.urls import path
import materials_app.views as views

app_name = 'materials_app'

urlpatterns = [
    path('', views.materials_view, name='materials'),
    path('add_material', views.MaterialAddView.as_view(), name='add_material'),
    path("update_material/<int:pk>/", views.MaterialUpdateView.as_view(), name="update_material"),
    path("delete_material/<int:pk>/", views.MaterialDeleteView.as_view(), name="delete_material"),
]