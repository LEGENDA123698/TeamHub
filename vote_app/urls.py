from django.urls import path
import vote_app.views as views


urlpatterns = [
    path('vote/', views.VotesView.as_view(), name='votes'),
    path("vote/detail/<int:pk>/", views.VoteDetailView.as_view(), name="detail_vote"),
    path("vote/create/", views.VoteCreateView.as_view(), name="create_vote"),
    path("vote/update/<int:pk>/", views.VoteUpdateView.as_view(), name="update_vote"),
    path("vote/delete/<int:pk>/", views.VoteDeleteView.as_view(), name="delete_vote"),
    path("vote/remove_vote/<int:pk>/", views.remove_vote, name="remove_vote_answer"),
]