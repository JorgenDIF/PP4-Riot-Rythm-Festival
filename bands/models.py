from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Genre choices
GENRE_CHOICES = (
    ('Rock', 'Rock'),
    ('Pop', 'Pop'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Indie', 'Indie'),
    ('Metal', 'Metal'),
    ('Electronic', 'Electronic'),
    ('RnB', 'RnB'),
    ('Blues', 'Blues'),
    ('Punk', 'Punk'),
    ('Disco', 'Disco'),
)


class Band(models.Model):
    band_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_name = models.CharField(max_length=255)
    genre_choices = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default='Rock'
    )

    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='bands/',
        force_format='WEBP',
        blank=False,
        null=False
    )
    image_alt = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField(max_length=5000)
    request_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.band_name)
        super(Band, self).save(*args, **kwargs)

    class Meta:
        ordering = ['band_name']

    def __str__(self):
        return self.band_name
