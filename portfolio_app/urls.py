from django.urls import path
import portfolio_app.views as views


urlpatterns = [
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="user_profile"),
    path("profile/friend_requests/", views.FriendRequestsView.as_view(), name="friend_requests"),
    path("profile/friend_request/<int:pk>/", views.friend_request, name="friend_request"),
    path("profile/add_friend/<int:pk>/", views.add_friend, name="add_friend"),
    path("profile/decline/<int:pk>/", views.decline, name="decline"),
    path("profile/delete_friend/<int:pk>/", views.delete_friend, name="delete_friend"),
    path("profile/portfolio/create/", views.PortfolioCreateView.as_view(), name="create_portfolio"),
    path("profile/portfolio/update/<int:pk>/", views.PortfolioUpdateView.as_view(), name="update_portfolio"),
    path("profile/portfolio/delete/<int:pk>/", views.PortfolioDeleteView.as_view(), name="delete_portfolio"),
    path("profile/update_avatar/<int:pk>/", views.AvatarUpdateView.as_view(), name="update_avatar"),
    path("profile/update_profile/<int:pk>/", views.ProfileUpdateView.as_view(), name="update_profile"),
]