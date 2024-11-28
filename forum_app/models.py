from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=50, blank=True)


class Theme(models.Model):
    name = models.CharField(max_length=50, blank=True)
    text = models.TextField(max_length=10000, blank=True)

class Message(models.Model):
    text = models.TextField(max_length=10000, blank=True)

