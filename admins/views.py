from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminCreateForm, UserAdminProfileForm


def index(request):
    return render(request, 'admins/admin.html')


def admin_user(request):
    users = User.objects.all()
    context = {
        'title': 'Geekshop - пользователи',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('admins:admin_user'))
        else:
            print(form.errors)
    else:
        form = UserAdminCreateForm()
    context = {
        'title': 'Админ - регистрация пользователей',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


def admin_user_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('admins:admin_user'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'Админ - Редактирование пользователя',
               'form': form,
               'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_user_activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


def admin_user_is_staff(request, id):
    user = User.objects.get(id=id)
    user.is_staff = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


def admin_user_delete_is_staff(request, id):
    user = User.objects.get(id=id)
    user.is_staff = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))
