

from django.urls import path
from .views import (
    AddBand,
    Bands,
    BandDetail,
    DeleteBand,
    EditBand,
    LikeBand


)

"""
URL patterns for the bands app.

This module defines the URL patterns for the bands app in the PP4
Riot Rythm Festival project.
"""

urlpatterns = [
    path("", AddBand.as_view(), name="add_band"),
    path("band_bank/", Bands.as_view(), name="band_bank"),
    path("bands/<int:pk>/<slug:slug>/", BandDetail.as_view(),
         name="band_detail"),
    path("bands/<int:pk>/<slug:slug>/delete/", DeleteBand.as_view(),
         name="delete_band"),
    path("bands/<int:pk>/<slug:slug>/edit/", EditBand.as_view(),
         name="edit_band"),
    path("bands/<int:pk>/<slug:slug>/like/", LikeBand.as_view(),
         name="like_band"),
]
