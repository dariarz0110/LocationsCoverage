from django.db import models

# Create your models here.

class location(models.Model):
    city = models.CharField(max_length=60, blank=False)
