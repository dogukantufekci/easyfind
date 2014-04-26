from django.db import models
from django.utils.translation import ugettext_lazy as _

from easyfind.models import AbstractModel


class Transaction(AbstractModel):
    PRICE_MAX_DIGITS = 8
    PRICE_DECIMAL_PLACES = 2

    buyer = models.ForeignKey('users.User', related_name='buyer_transactions', related_query_name='buyer_transaction', verbose_name=_("Buyer"))
    seller = models.ForeignKey('users.User', related_name='seller_transactions', related_query_name='seller_transaction', verbose_name=_("Seller"))
    offer = models.ForeignKey('offers.Offer', related_name='translations', related_query_name='translation', verbose_name=_("Offer"))
    amount = models.DecimalField(decimal_places=PRICE_DECIMAL_PLACES, max_digits=PRICE_MAX_DIGITS, verbose_name=_("Amount"))


    def __unicode__(self):
        return _(u"Transaction from {buyer} to {seller} in amount of ${amount} via Offer {offer}").format(
            buyer=self.buyer.get_full_name(), 
            seller=self.seller.get_full_name(), 
            amount=self.amount, 
            offer=self.offer.id,
        )