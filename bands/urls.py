from django.urls import path
from .views import (
    AddBand,
    Bands,
    AddBandRequest,
    BandDetail,
    DeleteBand,
    EditBand
)

urlpatterns = [
    path("", AddBand.as_view(), name="add_band"),
    path("band_bank/", Bands.as_view(), name="band_bank"),
    path("request_band/<slug:slug>/",
         AddBandRequest.as_view(), name="request_band"),
    path("bands/<slug:slug>/", BandDetail.as_view(), name="band_detail"),
    path("bands/<slug:slug>/delete/", DeleteBand.as_view(),
         name="delete_band"),
    path("bands/<slug:slug>/edit/", EditBand.as_view(), name="edit_band"),
]
