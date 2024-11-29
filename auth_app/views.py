from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('main-page')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main-page')
        else:
            print("FormNotValid")
    else:
        form = UserCreateForm()

    return render(request, 'auth_app/register.html', context = {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("login")
                return redirect('main-page')
            else:
                messages.error(request, 'invalid login or password')
    else:
        form = UserAuthForm()

    return render(request, 'auth_app/login.html', context = {'form': form})