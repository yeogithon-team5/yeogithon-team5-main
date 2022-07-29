from genericpath import exists
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.utils.crypto import get_random_string

def home(request):
    return render(request, 'calcapp/main.html')


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

def createGroup(request):
    if request.method == 'POST':
        group = Group()
        group.name = request.POST['name']
        group.owner = request.user
        group.code = str(request.user.id) + get_random_string(length=6)
        group.users.add(request.user)
        group.save()
    # else:
        # render(request, 'calcapp/create_group.html')

def deleteGroup(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    group.delete()
    return redirect('home')

def createPayment(request, group_id):
    # TODO: 프론트와 form 구조 추후 맞춰보기
    if request.method == 'POST':
        payment = Payment()
        group = get_object_or_404(Group, pk=group_id)
        payment.group = group
        payment.date = request.POST['date']
        payment.description = request.POST['description']
        payment.payer = User.objects.filter(pk=request.POST['payer'])
        div_type = request.POST['divide_type']
        payment.divide_type = div_type
        if div_type == '1/N' or not div_type:
            users = group.users_set.all()
            for user in users:
                ToPay.objects.create(
                    user = user,
                    amount = request.POST['amount']
                )
        else:
            topays = request.POST['topays']
            for topay in topays:
                ToPay.objects.create(
                    user = User.objects.filter(pk=topay['user']), # user id?
                    amount = topay['amount']
                )
    # else:
        # render(request, 'calcapp/create_payment.html')

def deletePayment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    group_id = payment.group.pk
    payment.delete()
    return redirect('createPayment', group_id=group_id)