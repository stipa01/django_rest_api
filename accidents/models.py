from django.db import models


class Accident(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, null=True, default='')  # description
    incident_type = models.CharField(max_length=100, blank=True, default='')
    incident_cause = models.CharField(max_length=200, blank=True, default='')
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    road_condition = models.CharField(max_length=500, blank=True, default='')
    incident_cost = models.IntegerField(null=True, default=0)
    license_number = models.CharField(max_length=50, blank=True, default='')
    temp = models.FloatField(blank=True, default=0)
    pressure = models.FloatField(blank=True, default=0)
    humidity = models.FloatField(blank=True, default=0)
    visibility = models.FloatField(blank=True, default=0)
    wind_speed = models.FloatField(blank=True, default=0)
    clouds = models.FloatField(blank=True, default=0)
    weather_description = models.TextField(blank=True, default='')
    # completed
    created_at = models.DateTimeField(auto_now_add=True)  # created_at

    def __str__(self):
        # return the task title
        return self.title
