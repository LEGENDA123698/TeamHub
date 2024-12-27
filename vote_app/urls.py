from django.urls import path
import vote_app.views as views

app_name = 'vote_app'

urlpatterns = [
    path('', views.VotesView.as_view(), name='votes'),
    path("detail/<int:pk>/", views.VoteDetailView.as_view(), name="detail_vote"),
    path("create/", views.VoteCreateView.as_view(), name="create_vote"),
    path("update/<int:pk>/", views.VoteUpdateView.as_view(), name="update_vote"),
    path("delete/<int:pk>/", views.VoteDeleteView.as_view(), name="delete_vote"),
    path("remove_vote/<int:pk>/", views.remove_vote, name="remove_vote_answer"),
]