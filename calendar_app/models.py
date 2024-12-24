from django.db import models
from colorfield.fields import ColorField
from django.urls import reverse


# модель события
class Event(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    date = models.DateField()
    color = ColorField(format="hex")
    def get_absolute_url(self):
        return reverse('calendar_app:event_detail', args=[str(self.id)])

