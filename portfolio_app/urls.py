from django.urls import path
import portfolio_app.views as views

app_name = 'portfolio_app'

urlpatterns = [
    path("<int:pk>/", views.ProfileView.as_view(), name="user_profile"),
    path("friend_requests/", views.FriendRequestsView.as_view(), name="friend_requests"),
    path("friend_request/<int:pk>/", views.friend_request, name="friend_request"),
    path("add_friend/<int:pk>/", views.add_friend, name="add_friend"),
    path("decline/<int:pk>/", views.decline, name="decline"),
    path("delete_friend/<int:pk>/", views.delete_friend, name="delete_friend"),
    path("portfolio/create/", views.PortfolioCreateView.as_view(), name="create_portfolio"),
    path("portfolio/update/<int:pk>/", views.PortfolioUpdateView.as_view(), name="update_portfolio"),
    path("portfolio/delete/<int:pk>/", views.PortfolioDeleteView.as_view(), name="delete_portfolio"),
    path("update_profile/<int:pk>/", views.ProfileUpdateView.as_view(), name="update_profile"),
]