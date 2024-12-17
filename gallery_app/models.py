from django.db import models
from django.core.validators import MaxValueValidator
from auth_app.models import User

class Image(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/gallery_images/')
    author = models.ForeignKey(User, related_name='image_author', on_delete=models.CASCADE)
    grid_column_span = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(2)],
        choices=[(1, '1'), (2, '2')]
    )
    grid_row_span = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(2)],
        choices=[(1, '1'), (2, '2')]
    )

    def __str__(self):
        return f'{self.title} by {self.author} ({self.id})'


