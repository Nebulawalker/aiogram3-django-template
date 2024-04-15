import requests

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import ContextMixin

from datetime import timedelta
from django.utils import timezone

from apps.custom_auth.views import LoginAbstractView, SignupAbstractView, LogoutAbstractView
from apps.custom_auth.models import CustomUser

from .models import User, UserLogs
from .forms import SignupForm, LoginForm


# Create your views here.

class AdminView(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('bot-admin:login')
    redirect_field_name = ''


class AdminDashboard(AdminView, generic.RedirectView):
    pattern_name = 'bot-admin:dashboard-overview'


class AdminDashboardOverview(AdminView, generic.TemplateView):
    template_name = 'bot/index.html'


class LoginView(LoginAbstractView):
    success_url = reverse_lazy('bot-admin:dashboard')
    login_url = reverse_lazy('bot-admin:dashboard')
    redirect_field_name = ''
    form_class = LoginForm
    template_name = 'bot/login.html'


class SignupView(SignupAbstractView):
    template_name = 'bot/index.html'
    login_url = reverse_lazy('bot-admin:dashboard')
    success_url = reverse_lazy('bot-admin:dashboard')
    redirect_field_name = ''
    model = CustomUser
    form_class = SignupForm


class LogoutView(LogoutAbstractView):
    login_url = reverse_lazy('bot-admin:login')
    redirect_field_name = ''
    pattern_name = 'main-page'

class ResetPasswordView(generic.FormView):
    pass


class VerifyEmailView(generic.FormView):
    pass
