from django.shortcuts import render


def index(request):
    return render(request, 'admins/admin.html')


def admin_user(request):
    return render(request, 'admins/admin-users-read.html')


def admin_user_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_user_delete(request):
    pass


def admin_user_update(request):
    return render(request, 'admins/admin-users-update-delete.html')
