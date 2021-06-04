from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
    gender = [('М', 'Мужской'), ('Ж', 'Женский')]
    sex = models.CharField(max_length=1, choices=gender, verbose_name='Пол')



