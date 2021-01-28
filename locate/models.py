from django.db import models


# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=60, blank=True)
    zipcode = models.PositiveSmallIntegerField(blank=True)


class CSVdata(models.Model):
    operator = models.PositiveSmallIntegerField
    lan = models.PositiveIntegerField
    lat = models.PositiveIntegerField
    o2g = models.BooleanField
    o3g = models.BooleanField
    o4g = models.BooleanField
