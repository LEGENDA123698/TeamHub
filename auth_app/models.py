from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_icons/', default='user_icons/user_icon.png')
    about = models.TextField(blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username