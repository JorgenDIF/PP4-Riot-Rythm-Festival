from django.urls import path
from .views import Profiles, EditProfile

"""
URL patterns for the bands app.

This module defines the URL patterns for the bands app in the PP4
Riot Rythm Festival project.
"""

urlpatterns = [
    path("user/<int:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<int:pk>/", EditProfile.as_view(), name="edit_profile"),
]
