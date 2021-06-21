from django import forms
from django.forms import ModelForm

from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from products.models import Product


class UserAdminCreateForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'image', 'email', 'password1', 'password2', 'gender')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductAdminForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5, 'style': 'vertical-align: middle;'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')
