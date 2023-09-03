from django.urls import path
from accounts.views import (
    UserCreateView,UserLoginView,
    LogoutView,UserProfileView,
)


urlpatterns = [
    path("registration/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
]
