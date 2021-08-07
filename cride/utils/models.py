"""Django models utilities."""
# from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext as _


class Base(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Última modificación'))
    description = models.TextField(blank=True, default="", verbose_name=_('Descripción'))
    alive = models.BooleanField(default=True, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Nombre"))
    # owner = models.ForeignKey(
    #     get_user_model(), 
    #     related_name="+",
    #     blank=True, null=True,
    #     verbose_name=_('Propietario')
    # )
    # last_edit_user = models.ForeignKey(
    #     get_user_model(),
    #     related_name="+",
    #     blank=True, 
    #     verbose_name=_('Modificado por')
    # )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        get_latest_by = 'creation_date'
        ordering = ['-creation_date', '-last_update']
