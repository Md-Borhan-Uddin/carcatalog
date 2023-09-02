from django.urls import path
from core.views import (
    HomeView,CarDetailView,
    CarCreateView
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("car/<int:pk>/<slug:slug>/", CarDetailView.as_view(), name="car_detail"),
    path("car/create/", CarCreateView.as_view(), name="car_create"),

]
