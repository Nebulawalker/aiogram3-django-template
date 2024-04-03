from django.db import models
from django.core.validators import MinLengthValidator

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

    def save(self, *args, **kwargs):
        if self.is_premium is None:
            self.is_premium = False

        super(User, self).save(*args, **kwargs)
