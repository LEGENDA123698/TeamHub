from django.db import models

class Thread(models.Model):
    name = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    #author = 