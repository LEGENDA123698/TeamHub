from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOISED = {
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    }

    PRIORITY_CHOISED = {
        ('low', 'Low'),
        ('medium', 'Meduim'),
        ('high', 'High')
    }

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOISED, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISED, default='medium')
    due_date = models.CharField(max_length=20, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Commect(models.Model):
    task = models.ForeignKey(Task, related_name='task', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()