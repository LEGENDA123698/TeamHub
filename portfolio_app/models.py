from django.db import models
from auth_app.models import User


class ShowcaseElement(models.Model):
    image = models.ImageField(upload_to='showcase_files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='showcase_elements')

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    valuable = models.BooleanField(default=False)