from django.urls import path
from .views import AddBand
urlpatterns = [
    path('', AddBand.as_view(), name='add_band')
]
