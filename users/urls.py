from django.urls import path

from users.views import UserLoginView, UserCreateView, UserLogoutView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

