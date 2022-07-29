from django.db import models
from account.models import User
# Create your models here.


class Group(models.Model):
    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='users')
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20, null=True)


class Payment(models.Model):
    group = models.ForeignKey(
        Group, related_name='payment', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=20)
    divide_type = models.CharField(default="1/n", max_length=5)
    payer = models.ForeignKey(
        User, related_name='payer', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    @property
    def amount_per_person(self):
        total = self.amount
        num = self.payer.count()
        return total/num


class ToPay(models.Model):
    payment = models.ForeignKey(
        Payment, related_name='topay', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='topay',
                             on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
