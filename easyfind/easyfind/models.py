from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("Created on"))
    updated_on = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Updated on"))

    class Meta:
        abstract = True