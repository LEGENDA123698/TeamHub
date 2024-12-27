from django.db import models
from colorfield.fields import ColorField


# модель события
class Event(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    date = models.DateField()
    color = ColorField(format="hex")
