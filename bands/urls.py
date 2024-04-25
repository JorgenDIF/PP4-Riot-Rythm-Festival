from django.urls import path
from .views import AddBand, Bands, AddBandRequest, BandDetail

urlpatterns = [
    path("", AddBand.as_view(), name="add_band"),
    path("band_bank/", Bands.as_view(), name="band_bank"),
    path("request_band/<slug:slug>/", AddBandRequest.as_view
         (), name="request_band"),
    path("bands/<slug:slug>/", BandDetail.as_view(), name="band_detail"),
]
