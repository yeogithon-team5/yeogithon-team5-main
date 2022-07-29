from django.shortcuts import render
from .models import *
import random

def createCode(request):
    # TODO: owner id + 코드로 만들기
    code = ''
    for i in range(3):
        rand = random.randrange(16, 256)
        code += hex(rand)[2:]

def createGroup(request):
    if request.method == 'POST':
        group = Group()
        group.name = request.POST['name']
        # TODO: 중복 코드인지 검사 
        group.code = createCode()
        
