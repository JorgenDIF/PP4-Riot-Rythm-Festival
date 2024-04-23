from django.views.generic import CreateView

from .models import Band


class AddBand(CreateView):
    """ Add band view """
    template_name = 'bands/add_band.html'
    model = Band
    success_url = '/bands/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBand, self).form_valid(form)


