from django.db import models
from auth_app.models import User


class Vote(models.Model):
    title = models.CharField(max_length=50)

class VoteAnswer(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='vote_images/', blank=True, null=True)
    procent = models.IntegerField(default=0)
    user = models.ManyToManyField(User, blank=True, related_name='users')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='vote_answers')
