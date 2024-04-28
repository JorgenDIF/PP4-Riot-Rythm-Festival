"""
URL patterns for the bands app.

This module defines the URL patterns for the bands app in the PP4
Riot Rythm Festival project.
"""

from django.urls import path
from .views import (
    AddBand,
    Bands,
    AddBandRequest,
    BandDetail,
    DeleteBand,
    EditBand,
    BandRequestDetail,
    ConfirmDeleteBandRequest,
    BandRequests,
    EditBandRequest,
    DeleteBandRequest
)

urlpatterns = [
    path("", AddBand.as_view(), name="add_band"),
    path("band_bank/", Bands.as_view(), name="band_bank"),
    path("request_band/", AddBandRequest.as_view(), name="request_band"),
    path("bands/<slug:slug>/", BandDetail.as_view(), name="band_detail"),
    path("bands/<slug:slug>/delete/", DeleteBand.as_view(),
         name="delete_band"),
    path("bands/<slug:slug>/edit/", EditBand.as_view(), name="edit_band"),
    path("band-request/<slug:slug>/", BandRequestDetail.as_view(),
         name="band_request_detail"),
    path("band-request/<slug:slug>/edit/", EditBandRequest.as_view(),
         name="edit_bandrequest"),
    path("band-request/<slug:slug>/delete/",
         ConfirmDeleteBandRequest.as_view(),
         name="confirm_delete_band_request"),
    path("band-requests/", BandRequests.as_view(), name="band_requests"),
    path("band-request/<slug:slug>/edit/", EditBandRequest.as_view(),
         name="edit_bandrequest"),
    path("band-request/<slug:slug>/delete/", DeleteBandRequest.as_view(),
         name="delete_bandrequest"),
]
