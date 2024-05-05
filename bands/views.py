from django.views import View
from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Band, Like
from .forms import BandsForm
from django.urls import reverse

from django.shortcuts import get_object_or_404, redirect


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

    def get_success_url(self):
        """
        Returns the URL to redirect to after the form is successfully
        validated.
        """
        return reverse('band_bank')

    def form_valid(self, form):
        """
        Validates the form data and saves the band.

        This method is called when the form data is valid.
        It sets the user attribute of the form
        instance to the current user and then calls
        the form_valid method of the parent class to save the form.
        """
        form.instance.user = self.request.user
        return super(AddBand, self).form_valid(form)


class BandDetail(LoginRequiredMixin, DetailView):
    """
    View for viewing a specific band.

    Inherits from LoginRequiredMixin and DetailView.
    """

    template_name = "bands/band_detail.html"
    model = Band
    context_object_name = "band"
    slug_url_kwarg = 'slug'


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
        band = self.get_object()
        return (self.request.user.is_superuser or
                band.user == self.request.user)


class DeleteBand(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a band.

    Inherits from LoginRequiredMixin and DeleteView.
    """
    model = Band
    success_url = "/bands/"

    def test_func(self):
        band = self.get_object()
        return (self.request.user.is_superuser or
                band.user == self.request.user)


class LikeBand(LoginRequiredMixin, View):
    """
    View for liking a band.

    Inherits from LoginRequiredMixin and View.
    """

    def post(self, request, pk, *args, **kwargs):
        print("Request method:", request.method)
        band = get_object_or_404(Band, pk=pk)
        Like.objects.get_or_create(user=request.user, band=band)
        return redirect('band_detail', pk=band.pk, slug=band.slug)
    
