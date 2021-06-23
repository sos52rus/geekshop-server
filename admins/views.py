from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator

from users.models import User
from admins.forms import UserAdminCreateForm, UserAdminProfileForm, ProductAdminForm
from products.models import Product


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexTemplateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser or u.is_staff)

class AdminUserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, **kwargs):
        context = super(AdminUserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserListView, self).dispatch(request, *args, **kwargs)


class AdminUserCreateView(CreateView):
    model = User
    form_class = UserAdminCreateForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_user')

    def get_context_data(self, **kwargs):
        context = super(AdminUserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Регистрация пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserCreateView, self).dispatch(request, *args, **kwargs)


class AdminUserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_user')

    def get_context_data(self, **kwargs):
        context = super(AdminUserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserUpdateView, self).dispatch(request, *args, **kwargs)


class AdminUserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('admins:admin_user')
    activate = False

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = self.activate
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserDeleteView, self).dispatch(request, *args, **kwargs)


class AdminUserActivateView(AdminUserDeleteView):
    activate = True




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


class AdminProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Товары'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductListView, self).dispatch(request, *args, **kwargs)


class AdminProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_product')

    def get_context_data(self, **kwargs):
        context = super(AdminProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Добавление товара'
        return context

    def post(self, request, *args, **kwargs):
        super(AdminProductCreateView, self).post(request, *args, **kwargs)
        if self.form_invalid(form=self.form_class):
            messages.success(request, 'Товар успешно создан')
            return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCreateView, self).dispatch(request, *args, **kwargs)


class AdminProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-product-update.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_product')

    def post(self, request, *args, **kwargs):
        super(AdminProductUpdateView,self).post(request, *args, **kwargs)
        if self.form_invalid(form=self.form_class):
            messages.success(request, 'Данные обновлены')
            return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(AdminProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Редактирование товара'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductUpdateView, self).dispatch(request, *args, **kwargs)


class AdminProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('admins:admin_product')
