from django.contrib import admin
from .models import Band, BandRequest


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = (
        "band_name",
        "genre_choices",
        "image",
    )
    list_filter = ("genre_choices",)


admin.site.register(BandRequest)
