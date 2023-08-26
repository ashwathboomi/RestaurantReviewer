from django.shortcuts import render
from rest_framework import generics, status
from .models import Restaurant
from .serializers import RestaurantSerializer, CreateRestaurantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class RestaurantViewer(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class GetRestaurant(APIView):
    serializer_class = RestaurantSerializer
    lookup_url_kwarg = "location"

    def get(self, request, format=None):
        location = request.GET.get(self.lookup_url_kwarg)
        if location != None:
            restaurants = Restaurant.objects.filter(location=location)
            if len(restaurants) > 0:
                lis = []
                for i in range(len(restaurants)):
                    data = RestaurantSerializer(restaurants[i]).data
                    lis.append(data)
                return Response(lis, status=status.HTTP_200_OK)
            return Response("Room Not Found", status=status.HTTP_404_NOT_FOUND)
        return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)


class CreateRestaurantViewer(APIView):
    serializer_class = CreateRestaurantSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data["name"]
            name_of_restaurant = serializer.data["name_of_restaurant"]
            location = serializer.data["location"]
            rating = serializer.data["rating"]
            review = serializer.data["review"]
            res = Restaurant(
                name=name,
                name_of_restaurant=name_of_restaurant,
                location=location,
                rating=rating,
                review=review,
            )
            res.save()
            return Response(
                RestaurantSerializer(res).data, status=status.HTTP_201_CREATED
            )
        return Response(
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
