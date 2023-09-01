from django.urls import path
from accounts.views import (
    UserCreateView,UserLoginView
)


urlpatterns = [
    path("registration/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
