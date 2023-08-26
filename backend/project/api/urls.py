from django.urls import path
from .views import RestaurantViewer, CreateRestaurantViewer, GetRestaurant

urlpatterns = [
    path("", RestaurantViewer.as_view()),
    path("review/", CreateRestaurantViewer.as_view()),
    path("get-res/", GetRestaurant.as_view()),
]
