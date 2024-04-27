from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Profile
from .forms import ProfileForm


class Profiles(TemplateView):
    """View for the profile page"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwarg):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            "profile": profile,
            "form": ProfileForm(instance=profile)

        }

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Profile"""

    form_class = ProfileForm
    model = Profile

    def get_template_names(self):
        return ['profiles/profile.html']

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.id == self.get_object().user.id
