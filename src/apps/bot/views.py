import requests

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import ContextMixin

from datetime import timedelta
from django.utils import timezone

from apps.custom_auth.views import LoginAbstractView, SignupAbstractView
from apps.custom_auth.models import CustomUser

from .models import User, UserLogs
from .forms import SignupForm, LoginForm


# Create your views here.

class AdminDashboardOverviewContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(AdminDashboardOverviewContext, self).get_context_data(**kwargs)
        active_users_this_week = (UserLogs.objects.filter(message_sent_datetime__gt=timezone.now() - timedelta(days=7)).
                                  values('user').distinct().count())
        active_users_last_week = (UserLogs.objects.filter(message_sent_datetime__gt=timezone.now() - timedelta(days=14),
                                                          message_sent_datetime__lt=timezone.now() - timedelta(days=7)).
                                  values('user').distinct().count())
        active_users_this_month = (
            UserLogs.objects.filter(message_sent_datetime__gt=timezone.now() - timedelta(days=30)).
            values('user').distinct().count())
        active_users_last_month = (
            UserLogs.objects.filter(message_sent_datetime__gt=timezone.now() - timedelta(days=60),
                                    message_sent_datetime__lt=timezone.now() - timedelta(days=30)).
            values('user').distinct().count())
        new_users_this_week = User.objects.filter(registration_date__gt=timezone.now() - timedelta(days=7)).count()
        new_users_last_week = User.objects.filter(registration_date__gt=timezone.now() - timedelta(days=14),
                                                  registration_date__lt=timezone.now() - timedelta(days=7)).count()
        new_users_this_month = User.objects.filter(registration_date__gt=timezone.now() - timedelta(days=30)).count()
        new_users_last_month = User.objects.filter(registration_date__gt=timezone.now() - timedelta(days=60),
                                                   registration_date__lt=timezone.now() - timedelta(days=30)).count()
        new_messages_today = UserLogs.objects.filter(
            message_sent_datetime__gt=timezone.now() - timedelta(days=1)).count()

        try:
            quotation = requests.get(settings.JOKE_API_URL, timeout=settings.REQUEST_TIMEOUT).text
        except requests.exceptions.ConnectionError:
            quotation = None

        context.update({
            '7_days_new_users': User.objects.filter(registration_date__gt=timezone.now() - timedelta(days=7)),
            'active_users_this_week': active_users_this_week,
            'active_users_last_week': active_users_last_week,
            'active_users_this_month': active_users_this_month,
            'active_users_last_month': active_users_last_month,
            'new_users_this_month': new_users_this_month,
            'new_users_last_month': new_users_last_month,
            'new_users_this_week': new_users_this_week,
            'new_users_last_week': new_users_last_week,
            'new_messages_today': new_messages_today,
            'quotation': quotation
        })
        print(context)
        return context


class AdminDashboardRedirectView(generic.RedirectView):
    pattern_name = 'bot-admin:dashboard-overview'


def dashboard(request):
    success_redirect = 'bot-admin:dashboard-overview'
    unsuccess_redirect = ''

    if request.user.is_authenticated:
        print('asd+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    else:
        print('asd')


def dashboard_overview(request):
    pass


# class AdminDashboardView(AdminDashboardAbstractView):
#     template_name = 'bot/index.html'
#     redirect_field_name = ''
#     login_url = reverse_lazy('bot-admin:login')


# class AdminDashboardOverviewView(AdminDashboardOverviewContext, AdminDashboardView):
#     pass


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


class ResetPasswordView(generic.FormView):
    pass


class VerifyEmailView(generic.FormView):
    pass
