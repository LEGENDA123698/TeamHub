from django.db import models


# модель события
class Event(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    date = models.DateField()
