# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _

# Utilities
from cride.utils.models import Base


class Circle(Base):
    """A circle is a private grooup where rides are offered and taken
    by its members. To join a circle a user must reveive an unique invtation 
    code from an existing circle member"""
    slug_name = models.SlugField(unique=True, max_length=40)
    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        "Verified circle",
        default=False,
        help_text='Verified circles are also known as official communities.'
    )
    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone know about their existence.'
    )
    is_limited = models.BooleanField('Limited', default=False, 
        help_text='Limited circles can grow up to a fiexd number of members')
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members.'
    )

    class Meta(Base.Meta):
        """Meta class."""
        ordering = ['-rides_taken', '-rides_offered']


