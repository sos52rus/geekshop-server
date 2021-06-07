from django.urls import path

from users.views import user_auth, user_register, logout

app_name = 'users'

urlpatterns = [
    path('login/', user_auth, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', logout, name='logout'),
]

