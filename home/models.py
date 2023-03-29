from django.db import models
from math import sin, cos, sqrt, atan2, radians
class Shop(models.Model):
    shop_name=models.CharField(max_length=100)
    shop_type=models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return f'{self.shop_name} {self.shop_type}'
    def distance_to(self, user_latitude, user_longitude):
        R = 6371  # Earth radius in km

        lat1, lon1 = radians(self.latitude), radians(self.longitude)
        lat2, lon2 = radians(user_latitude), radians(user_longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))

        distance = R * c  # Distance in km
        return distance