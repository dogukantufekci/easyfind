from geoposition.fields import GeopositionField

from django.db import models
from django.utils.translation import ugettext_lazy as _

from easyfind.models import AbstractModel


class Job(AbstractModel):
    buyer = models.ForeignKey('users.User', related_name='jobs', related_query_name='job', verbose_name=_("Buyer"))
    title = models.ForeignKey('sellers.Title', related_name='jobs', related_query_name='job', verbose_name=_("Title"))
    geoposition = GeopositionField(verbose_name=_("Geoposition"))
    start_on = models.DateTimeField(verbose_name=_("Start on"))
    start_asap = models.BooleanField(default=False, verbose_name=_("Start ASAP"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))


    class Meta:
        ordering = ('buyer', '-is_active', '-created_on',)


    def __unicode__(self):
        return _(u"{buyer} needs a {title}").format(buyer=self.buyer.get_full_name(), title=self.title.title)