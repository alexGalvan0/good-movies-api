from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    # profile_picture = models.ImageField( blank=True)
    date_joined = models.DateField(auto_now=True)

    REQUIRED_FIELDS = []