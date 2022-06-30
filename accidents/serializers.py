from rest_framework import routers, serializers, viewsets
from .models import Accident


class AccidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accident
        fields = ['id', 'title', 'description', 'incident_type', 'incident_cause', 'lat', 'long', 'road_condition',
                  'incident_cost', 'license_number', 'temp', 'pressure', 'humidity', 'visibility', 'wind_speed',
                  'clouds', 'weather_description', 'created_at']
