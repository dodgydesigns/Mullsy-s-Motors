# ,,,,,,,,,,
from django.conf import settings
from django.db import models


class Rental(models.Model):
    """
    Represents the fields required for each rental
    """

    rental_id = models.IntegerField(default=-1)
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_email = models.EmailField()
    vehicle_vin = models.CharField(max_length=17)
    vehicle_make = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    rental_start_date = models.DateField()
    rental_duration = models.FloatField()  # Assume partial days are allowed
    rental_day_rate = models.FloatField()
    paid = models.CharField(max_length=20)
