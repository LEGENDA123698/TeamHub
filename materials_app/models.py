from django.db import models
from urllib.parse import urlparse, parse_qs


material_types = (
    ('LINK', 'link'),
    ('VIDEO', 'video'),
    ('FILE', 'file'),
    ('IMAGE', 'image'),
)


class Material(models.Model):
    description = models.TextField()
    link = models.TextField(blank=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    type = models.CharField(max_length=20, choices=material_types,default='LINK')

    def cut_url(self):
        url = self.link
        if "youtu.be" in url:
            self.link = url.split("/")[-1]
        elif "youtube.com" in url:
            query = urlparse(url).query
            self.link = parse_qs(query).get("v", [None])[0]
        else:
            return self.link

    def save(self, *args, **kwargs):
        if self.type == 'VIDEO':
            self.cut_url()
        super().save(*args, **kwargs)