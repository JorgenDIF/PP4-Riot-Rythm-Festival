from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Band


class BandsForm(forms.ModelForm):
    """
    A form for creating or updating a band.

    This form is used to collect information about a band,
    such as the band name,
    description, motivation, genre choices, image, and image alt text.
    """

    class Meta:
        model = Band
        fields = ["band_name", "description", "motivation",
                  "genre_choices", "image", "image_alt"]

    description = forms.CharField(widget=RichTextWidget())
    motivation = forms.CharField(widget=RichTextWidget())

    labels = {
        "band_name": "Band Name",
        "description": "Description",
        "motivation": "Motivation",
        "genre_choices": "Genre",
        "image": "Image",
        "image_alt": "Image Alt",
    }
