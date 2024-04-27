from django.views.generic import TemplateView

from .models import Profile


class Profiles(TemplateView):
    """ View for the profile page   """
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwarg):
        profile = Profile.objects.get(user=self.kwargs['pk'])
        context = {
            'profile': profile
        }

        return context
