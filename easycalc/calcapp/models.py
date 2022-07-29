from django.db import models
from account.models import *

class Group(models.Model):
    user = models.ManyToManyField(related_name='groups')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)

class Payment(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=30)
    divide_type = models.CharField(max_length=10, default='1/N')
    payer = models.ForeignKey(User, on_delete=models.CASCADE)

class ToPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)