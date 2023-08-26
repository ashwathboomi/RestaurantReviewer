from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, default="")
    name_of_restaurant = models.CharField(max_length=50, default="")
    time = models.DateField(auto_now=True)
    location_choices = [
        ("BX", "Bronx"),
        ("BN", "Brooklyn"),
        ("MN", "Manhattan"),
        ("SI", "Staten Island"),
        ("QN", "Queens"),
    ]
    location = models.CharField(max_length=2, choices=location_choices, default="MN")
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=50
    )
    review = models.CharField(max_length=500, default="")
