from django.db import models
from urllib.parse import urlparse, parse_qs


class Link_Model(models.Model):
    description = models.TextField()
    link = models.TextField()

class Video_Model(models.Model):
    description = models.TextField()
    link = models.TextField()

    def cut_url(self):
        url = self.link
        if "youtu.be" in url:
            self.link = url.split("/")[-1]
        elif "youtube.com" in url:
            query = urlparse(url).query
            self.link = parse_qs(query).get("v", [None])[0]
        else:
            self.link

    def save(self, *args, **kwargs):
        self.cut_url()
        super().save(*args, **kwargs)

class File_Model(models.Model):
    description = models.TextField()
    file = models.FileField(upload_to='files/',)

class Image_Model(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/',)