from django.db import models
from auth_app.models import User

class Notification(models.Model):

    title = models.CharField(max_length=30, default='title')
    text = models.TextField(max_length=500) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    seen_users = models.ManyToManyField(User, blank=True, related_name='seen_users')