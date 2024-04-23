from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Band
from .forms import BandsForm


class AddBand(LoginRequiredMixin, CreateView):
    """ Add band view """
    template_name = 'bands/add_band.html'
    model = Band
    form_class = BandsForm
    success_url = '/bands/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBand, self).form_valid(form)
