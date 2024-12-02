from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):

    text = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)