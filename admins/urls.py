from django.urls import path

from admins.views import admin_user, admin_user_create, admin_user_delete, admin_user_update, index, \
    admin_user_activate, admin_user_delete_is_staff, admin_user_is_staff


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user, name='admin_user'),
    path('users/create/', admin_user_create, name='admin_user_create'),
    path('users/update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('users/delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('users/activate/<int:id>/', admin_user_activate, name='admin_user_activate'),
    path('users/is_staff/<int:id>/', admin_user_is_staff, name='admin_user_is_staff'),
    path('users/delete_is_staff/<int:id>/', admin_user_delete_is_staff, name='admin_user_delete_is_staff'),

]
