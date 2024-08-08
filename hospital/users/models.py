from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/', default='default_user_icon.png')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

