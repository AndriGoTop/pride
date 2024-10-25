from modulefinder import Module

from django.db import models

class Tools(models.Module):
    title = models.CharField(max_length=30)
    price_ym = models.IntegerField()
