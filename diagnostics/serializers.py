from rest_framework import routers,serializers,viewsets
from .models import Diagnostic


class DiagnosticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnostic
        fields = ['id', 'title', 'description', 'alarm', 'created_at']
