from django.contrib import admin
from .models import Band


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = (
        "band_name",
        "genre_choices",
        "image",
        "user",
    )
    list_filter = ("genre_choices",)
