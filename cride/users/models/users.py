from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _

from cride.utils.models import Base


class User(Base, AbstractUser):
    email = models.EmailField(
        'email address',
        unique = True,
        error_messages = {
            'unique': 'A user with that email already exists.'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message = 'phone number must be entered in the format +999999999. Up to 15 digits allowed'
    )
    phone_number = models.CharField(
        validators = [phone_regex],
        max_length = 17,
        blank = True
    )
    is_client = models.BooleanField(
        'client status', 
        default=True,
        help_text=('Help easily distinguish users and perform queries.'
        'clients are the main type of users.'
        )
    )
    is_verified = models.BooleanField(
        'client status', 
        default=False,
        help_text=(
            'Set to true when the user have verified its email address.'
        )
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username
