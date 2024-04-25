from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Band, BandRequest
from .forms import BandsForm, BandRequestForm

from django.shortcuts import redirect


class Bands(ListView):
    """_View all bands_"""

    template_name = "bands/band_bank.html"
    model = Band
    context_object_name = "bands"
    ordering = ["band_name"]


class AddBand(LoginRequiredMixin, CreateView):
    """
    View for adding a new band.

    Inherits from LoginRequiredMixin and CreateView.
    """

    template_name = "bands/add_band.html"
    model = Band
    form_class = BandsForm
    success_url = "/bands/"

    def form_valid(self, form):
        """
        Validates the form data and saves the band.

        If the user is not a superuser, redirects to the home page.
        Sets the user field of the band instance to the current user.
        """
        if not self.request.user.is_superuser:
            return redirect("home")
        form.instance.user = self.request.user
        return super(AddBand, self).form_valid(form)


class AddBandRequest(LoginRequiredMixin, CreateView):
    """
    View for adding a new band request.

    Inherits from LoginRequiredMixin and CreateView.
    """

    template_name = "bands/add_band_request.html"
    model = BandRequest
    form_class = BandRequestForm
    success_url = "/bands/"

    def form_valid(self, form):
        """
        Validates the form data and saves the band request.

        Sets the user field of the band request instance to the current user.
        """
        form.instance.user = self.request.user
        return super(AddBandRequest, self).form_valid(form)


class BandDetail(LoginRequiredMixin, DetailView):
    """
    View for viewing a specific band.

    Inherits from LoginRequiredMixin and DetailView.
    """

    template_name = "bands/band_detail.html"
    model = Band
    context_object_name = "band"
    slug_url_kwarg = "slug"


class EditBand(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing a band.

    Inherits from LoginRequiredMixin and UpdateView.
    """

    template_name = "bands/edit_band.html"
    model = Band
    form_class = BandsForm
    success_url = "/bands/"

    def test_func(self):
        return self.request.user.is_superuser


class DeleteBand(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a band.

    Inherits from LoginRequiredMixin and DeleteView.
    """
    model = Band
    success_url = "/bands/"

    def test_func(self):
        return self.request.user.is_superuser
