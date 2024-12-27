from django.db import models
from auth_app.models import User


note_types = (
    ('HOMEWORK', 'homework'),
    ('CLASSWORK', 'classwork'),
    ('PROJECT', 'project'),
)

class Theme(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Note(models.Model):
    note = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=20, choices=note_types,)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
