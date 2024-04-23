from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Band


class BandsForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['band_name',
                  'description', 'genre_choices', 'image', 'image_alt', ]

    description = forms.CharField(widget=RichTextWidget())

    widget = {
        'description': forms.Textarea(attrs={'rows': 5}),
    }

    labels = {
        'band_name': 'Band Name',
        'description': 'Description',
        'genre_choices': 'Genre',
        'image': 'Image',
        'image_alt': 'Image Alt'
    }
