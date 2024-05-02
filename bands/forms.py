from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Band


class BandsForm(forms.ModelForm):
    """
    A form for creating or updating a band.

    This form is used to collect information about a band,
    such as the band name,
    description, genre choices, image, and image alt text.
    """

    class Meta:
        model = Band
        fields = ["band_name", "description",
                  "genre_choices", "image", "image_alt"]

    description = forms.CharField(widget=RichTextWidget())

    widgets = {
        "description": forms.Textarea(attrs={"rows": 5}),
    }

    widgets = {
        "motivation": forms.Textarea(attrs={"rows": 5}),
    }

    labels = {
        "band_name": "Band Name",
        "description": "Description",
        "genre_choices": "Genre",
        "image": "Image",
        "image_alt": "Image Alt",
    }


