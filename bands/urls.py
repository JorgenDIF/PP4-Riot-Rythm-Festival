from django.urls import path
from .views import AddBand, Bands

urlpatterns = [
    path('', AddBand.as_view(), name='add_band'),
    path('band_suggestions/', Bands.as_view(), name='band.suggestions'),
]