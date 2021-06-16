from django.urls import path

from admins.views import admin_user, admin_user_create, admin_user_delete, admin_user_update, index

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user, name='admin_user'),
    path('users/create/', admin_user_create, name='admin_user_create'),
    path('users/update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('users/delete/<int:id>/', admin_user_delete, name='admin_user_delete')
]
