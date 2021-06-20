from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminCreateForm, UserAdminProfileForm, ProductAdminForm
from products.models import Product


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_user(request):
    users = User.objects.all()
    context = {
        'title': 'Geekshop - пользователи',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_user_activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


@user_passes_test(lambda u: u.is_superuser)
def admin_user_is_staff(request, id):
    user = User.objects.get(id=id)
    user.is_staff = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete_is_staff(request, id):
    user = User.objects.get(id=id)
    user.is_staff = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_user'))


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_product(request):
    products = Product.objects.all()
    context = {
        'title': 'Админ - Продукты',
        'products': products
    }
    return render(request, 'admins/admin-products.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан.')
            return HttpResponseRedirect(reverse('admins:admin_product'))
        else:
            print(form.errors)
    else:
        form = ProductAdminForm()
    context = {
        'title': 'Админ - Добавление товара',
        'form': form,
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_product_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES, instance=selected_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = ProductAdminForm(instance=selected_product)
    context = {'title': 'Админ - Редактирование товара',
               'form': form,
               'selected_product': selected_product}
    return render(request, 'admins/admin-product-update.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_product'))
