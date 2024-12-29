from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/user_icons/', default='media/user_icons/user_icon.png')
    about = models.CharField(max_length=210,blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username