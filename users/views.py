from django.contrib import auth, messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator

from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basket.models import Basket


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context.update({'title': 'Geekshop - Авторизация'})
        return context


class UserCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Geekshop - Регистраци'})
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Geekshop - Редактирование профиля',
            'baskets': Basket.objects.filter(user=self.request.user),
        })
        return context

    def get_success_url(self):
        success_url = reverse_lazy('users:profile', kwargs={'pk': self.object.pk})
        return success_url

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserLogoutView, self).dispatch(request, *args, **kwargs)
