from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main')
    else:
        form = AuthenticationForm()
        return render(request, "account/login.html", {'form': form})


def signup(request):
    if request.user_is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
        return render(request, 'account/signup.html', {'form': form})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('index')
    return redirect('signup')
