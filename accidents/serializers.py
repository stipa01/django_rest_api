from rest_framework import routers, serializers, viewsets
from .models import Accident


class AccidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accident
        fields = ['id', 'title', 'description', 'severe', 'created_at']
