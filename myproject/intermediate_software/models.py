
from django.db import models

class DeviceData(models.Model):
    time = models.BigIntegerField()
    packet_type = models.IntegerField()
    device_id = models.IntegerField()
    device_type = models.IntegerField()
    device_latitude = models.FloatField()
    device_longitude = models.FloatField()
    device_altitude = models.FloatField()