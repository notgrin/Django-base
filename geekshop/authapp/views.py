from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginFrom, UserRegisterFrom


def login(request):
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginFrom()
    context = {
        'title': 'Geekshop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterFrom()

    context = {
        'title': 'Geekshop | Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
