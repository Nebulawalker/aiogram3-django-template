from django import forms
from django.contrib.auth import login, authenticate
from django.core.validators import RegexValidator
from django.conf import settings

from django.contrib import messages

from apps.custom_auth.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[RegexValidator('^[a-zA-Z0-9]*$')])
    is_remember = forms.BooleanField(widget=forms.CheckboxInput, required=False)


    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        super(LoginForm, self).__init__(*args, **kwargs)

    def authenticate(self):
        if not self.request.user.is_authenticated:
            try:
                username = CustomUser.objects.get(email=self.data['email']).username
            except CustomUser.DoesNotExist:
                username = None

            user = authenticate(request=self.request,
                                username=username,
                                password=self.data['password'])

            if user:
                if not self.data.get('is_remember'):
                    self.request.session.set_expiry(settings.MIN_SESSION_COOKIE_TIME)

                login(self.request, user)
            else:
                messages.add_message(self.request, messages.ERROR, 'Invalid data.', fail_silently=True)
    



class SignupForm(forms.Form):
    pass