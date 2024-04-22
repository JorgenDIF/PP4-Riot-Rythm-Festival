from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

class Band(models.Model):
    band_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    image= ResizedImageField(
        size=[400, None], quality=75, upload_to='bands/', force_format='WEBP',
        blank=False, null=False
    )
    image_alt = models.CharField(max_length=255)
    description = RichTextField(max_length=5000)
    request_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.band_name)
        super(Band, self).save(*args, **kwargs)

    def __str__(self):
        return self.band_name
