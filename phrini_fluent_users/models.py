from django.db import models
from django.contrib.auth.models import AbstractUser


class PhriniFluentUser(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    telegram_handle = models.CharField(
        max_length=100, unique=True, null=True, blank=True
    )
