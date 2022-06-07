from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
