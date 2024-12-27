from django.urls import path
import diary_app.views as views

app_name = 'diary_app'

urlpatterns = [
    path('<int:user_pk>/', views.DiaryView.as_view(), name='diary'),
    path('update/<int:user_pk>/<int:theme_pk>', views.DiaryView.as_view(), name='update'),
    path('add_note/<int:user_pk>/<int:theme_pk>', views.DiaryView.as_view(), name='add_note'),
    path('delete/<int:user_pk>/<int:pk>', views.ThemeDeleteView.as_view(), name='delete'),
    path('delete_note/<int:user_pk>/<int:pk>', views.NoteDeleteView.as_view(), name='delete_note'),
]