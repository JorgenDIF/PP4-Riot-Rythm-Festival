from django.urls import path
from .views import AddBand, Bands

urlpatterns = [
    path('', AddBand.as_view(), name='add_band'),
    path('band_bank/', Bands.as_view(), name='band_bank'),
]