# logapp/models.py
from django.db import models

class LogEntry(models.Model):
    measurement_time = models.DateTimeField(auto_now_add=True)
    upper_power2 = models.FloatField()
    upper_snr = models.FloatField()
    lower_power = models.FloatField()
    lower_snr = models.FloatField()
    cell_number = models.CharField(max_length=50)

