from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreAPIView,
    MovieViewSet,
    GenreDetailAPIView,
    ActorAPIView,
    ActorDetailAPIView
)

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
    "patch": "partial_update"
})
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("cinema-hall/", cinema_hall_list, name="cinema_list"),
    path("cinema-hall/<int:pk>", cinema_hall_detail, name="cinema_detail"),
    path("", include(router.urls)),
    path("genres/", GenreAPIView.as_view(), name="genres"),
    path("genres/<int:pk>", GenreDetailAPIView.as_view(), name="genres"),
    path("actors/", ActorAPIView.as_view(), name="actors"),
    path("actors/<int:pk>", ActorDetailAPIView.as_view(), name="actors"),
]

app_name = "cinema"
