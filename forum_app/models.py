from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=50, blank=True)


class Theme(models.Model):
    name = models.CharField(max_length=50, blank=True)
    text = models.TextField(max_length=10000, blank=True)
    author = models.ForeignKey(User, related_name="theme_author", on_delete=models.CASCADE)

class Message(models.Model):
    text = models.TextField(max_length=10000, blank=True)
    message_author = models.ForeignKey(User, related_name="message_author", on_delete=models.CASCADE)

