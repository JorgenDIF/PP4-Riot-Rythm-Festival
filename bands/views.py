
from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Band
from .forms import BandsForm

from django.shortcuts import redirect


class Bands(ListView):
    """_View all bands_"""
    template_name = 'bands/band_bank.html'
    model = Band
    context_object_name = 'bands'
    ordering = ['band_name']


class AddBand(LoginRequiredMixin, CreateView):
    """
    View for adding a new band.

    Inherits from LoginRequiredMixin and CreateView.
    """

    template_name = 'bands/add_band.html'
    model = Band
    form_class = BandsForm
    success_url = '/bands/'

    def form_valid(self, form):
        """
        Validates the form data and saves the band.

        If the user is not a superuser, redirects to the home page.
        Sets the user field of the band instance to the current user.
        """
        if not self.request.user.is_superuser:
            return redirect('home')
        form.instance.user = self.request.user
        return super(AddBand, self).form_valid(form)
