from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "name_of_restaurant",
            "time",
            "location",
            "rating",
            "review",
        )


class CreateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("name", "name_of_restaurant", "location", "rating", "review")
