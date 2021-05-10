from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse


class Login(LoginView):
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):

        user = self.request.user
        url = self.get_redirect_url()
        return url or resolve_url(reverse('profile', kwargs={'nom': user.username}))
