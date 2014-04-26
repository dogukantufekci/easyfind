from geoposition.fields import GeopositionField

from django.db import models
from django.utils.translation import ugettext_lazy as _

from easyfind.models import AbstractModel


class Transaction(AbstractModel):
    buyer = models.ForeignKey('users.User', related_name='transactions', related_query_name='job', verbose_name=_("Buyer"))
    seller = models.ForeignKey('users.User', related_name='transactions', related_query_name='job', verbose_name=_("Title"))
    geoposition = GeopositionField(verbose_name=_("Geoposition"))
    start_on = models.DateTimeField(verbose_name=_("Start on"))
    start_asap = models.BooleanField(default=False, verbose_name=_("Start ASAP"))


    def __unicode__(self):
        return _(u"{buyer} needs a {title}").format(buyer=self.buyer.get_full_name(), title=self.title.title)