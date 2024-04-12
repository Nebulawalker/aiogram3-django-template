from abc import ABC

from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from utils.mixins.not_logged import NotLoggedRequired


# Create your views here.

class LoginAbstractView(ABC, NotLoggedRequired, generic.FormView):
    def get_form_kwargs(self):
        kwargs = super(LoginAbstractView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.authenticate()
        return super(LoginAbstractView, self).form_valid(form)


class SignupAbstractView(ABC, NotLoggedRequired, generic.CreateView):
    pass


class ResetPasswordAbstractView(ABC, LoginRequiredMixin, generic.FormView):
    pass


class VerifyEmailAbstractView(ABC, generic.FormView):
    pass
