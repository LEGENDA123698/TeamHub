from django.db import models
from django.urls import reverse
from auth_app.models import User
from colorfield.fields import ColorField

class Section(models.Model):
    name = models.CharField(max_length=50, blank=True)
    tag = models.CharField(max_length=10, blank=True)
    tag_color = ColorField(format="hex", blank=True)
    def get_absolute_url(self):
        return reverse('forum_app:section_detail', args=[str(self.id)])

class Theme(models.Model):
    name = models.CharField(max_length=50, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="themes")
    text = models.TextField(max_length=10000, blank=True)
    author = models.ForeignKey(User, related_name="theme_author", on_delete=models.CASCADE, blank=True)
    related_section = models.ForeignKey(Section, related_name="section_theme", on_delete=models.CASCADE, blank=True)
    tag = models.CharField(max_length=10, blank=True)
    tag_color = ColorField(format="hex", blank=True)
    
    
    def get_absolute_url(self):
        return reverse('forum_app:theme_detail', args=[str(self.id)])


    
class Message(models.Model):
    message_author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='messages/', null=True, blank=True)
    related_theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('forum_app:message_detail', args=[str(self.id)])