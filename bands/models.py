from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Genre choices
GENRE_CHOICES = (
    ("Rock", "Rock"),
    ("Pop", "Pop"),
    ("Hip-Hop", "Hip-Hop"),
    ("Indie", "Indie"),
    ("Metal", "Metal"),
    ("Electronic", "Electronic"),
    ("RnB", "RnB"),
    ("Blues", "Blues"),
    ("Punk", "Punk"),
    ("Disco", "Disco"),
)


class Band(models.Model):
    """
    A model representing a band with inspiration from the Macs YouTube video.
    Link to video is in the README.md file.
    """

    band_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_name = models.CharField(max_length=255)
    genre_choices = models.CharField(
        max_length=50, choices=GENRE_CHOICES, default="Rock"
    )

    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="bands/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField(max_length=5000)
    motivation = RichTextField(max_length=5000, default='Default motivation')
    request_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.band_name)
        super(Band, self).save(*args, **kwargs)

    def count_likes(self):
        return Like.objects.filter(band=self).count()

    class Meta:
        ordering = ["band_name"]

    def __str__(self):
        return self.band_name


class Like(models.Model):
    """
    Represents a like given by a user to a band.
    Insspired by example on stackoverflow. Link in README.md file.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="likes")
    band = models.ForeignKey(Band, on_delete=models.CASCADE,
                             related_name="liked_by")
    liked_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'band')

    def __str__(self):
        return f"{self.user.username} likes {self.band.band_name}"
