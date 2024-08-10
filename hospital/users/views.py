from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User
from users.forms import SignupForm


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/profile.html'


class SignupView(generic.CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
