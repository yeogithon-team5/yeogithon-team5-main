from django.shortcuts import render
from .models import *
from django.utils.crypto import get_random_string

def createGroup(request):
    if request.method == 'POST':
        group = Group()
        group.name = request.POST['name']
        group.owner = request.user
        group.code = str(request.user.id) + get_random_string(length=6)
        group.users.add(request.user)
        group.save()
    # else:
        # render(request, 'calcapp/creategroup.html')

