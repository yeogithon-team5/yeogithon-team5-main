from genericpath import exists
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.utils.crypto import get_random_string

# Create your views here.


def calc_result(request, pk):
    group = get_object_or_404(Group, pk=pk)
    users = group.user.all()
    payments = group.payment.all()
    ret = {}
    for u in users:
        ret[u.username] = 0
    for p in payments:
        topay = p.topay.all()
        for t in topay:
            ret[t.user.username] += t.amount
    return render(request, "ex.html", {'users': users, 'payments': payments, 'ret': ret})
