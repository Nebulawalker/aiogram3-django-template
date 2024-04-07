from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from utils.validators.time import only_past_datetime


# Create your models here.

class User(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=32, validators=[MinLengthValidator(4)], null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_premium = models.BooleanField()
    registration_date = models.DateTimeField(auto_now_add=True, validators=[only_past_datetime])
    last_activity = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()

        if self.last_name is not None:
            self.last_name = self.last_name.capitalize()

        if self.is_premium is None:
            self.is_premium = False

        super(User, self).save(*args, **kwargs)


class UserLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    message_body = models.CharField(max_length=4096)
    message_sent_datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.message_body is None:
            self.message_body = 'Is not text.'

        super(UserLogs, self).save(*args, **kwargs)
