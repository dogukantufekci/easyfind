from django.db import models
from django.utils.translation import ugettext_lazy as _


from easyfind.models import AbstractModel

from .choices import Statuses


class Offer(AbstractModel):
    PRICE_MAX_DIGITS = 8
    PRICE_DECIMAL_PLACES = 2

    job = models.ForeignKey('jobs.Job', related_name='offers', related_query_name='offer', verbose_name=_("Job"))
    seller = models.ForeignKey('sellers.Seller', related_name='offers', related_query_name='offer', verbose_name=_("Seller"))
    price = models.DecimalField(decimal_places=PRICE_DECIMAL_PLACES, max_digits=PRICE_MAX_DIGITS, verbose_name=_("Price"))
    status = models.PositiveIntegerField(choices=Statuses.CHOICES, default=Statuses.WAITING,verbose_name=_("Status"))
    

    def __unicode__(self):
        return _(u"{seller}'s offer for Job {job} is {price}").format(seller=self.seller.user.get_full_name(), job=self.job.id, price=self.price)