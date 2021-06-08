from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def user_auth(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShoop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'GeekShoop - Регистрация',
        'form': form,
    }
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profiler'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'GeekShop - Профиль',
               'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
