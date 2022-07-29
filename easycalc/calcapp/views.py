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
    for u1 in users:
        payer = {}
        for u2 in users:
            if u1 != u2:
                payer[u2.username] = 0
        ret[u1.username] = payer

    print(ret)
    for p in payments:
        topay = p.topay.all()
        for t in topay:
            ret[p.payer.username][t.user.username] += t.amount
    return render(request, "ex.html", {'ret': ret})
