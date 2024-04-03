from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


def only_past_datetime(value: datetime):
    if value > timezone.now():
        raise ValidationError(
            _("The date have to be in past"),
        )