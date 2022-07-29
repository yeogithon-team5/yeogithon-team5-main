from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    bank = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20)
