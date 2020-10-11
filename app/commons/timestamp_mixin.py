from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampMixin(models.Model):
    created = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('last updated'), auto_now=True)

    class Meta:
        abstract = True