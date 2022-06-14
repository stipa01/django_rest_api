from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        # create and return a new user
        pass

    def create_superuser(self, email, password):
        # create and return a new superuser
        pass


class MyCustomUser(AbstractBaseUser):
    # add your custom fields here
    pass
