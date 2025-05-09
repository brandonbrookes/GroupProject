from django.db import models

class AirQuality(models.Model):
    pm1 = models.IntegerField()
    pm2 = models.IntegerField()
    pm3 = models.IntegerField()
    date = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
