from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
