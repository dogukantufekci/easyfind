from geoposition.fields import GeopositionField

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from easyfind.models import AbstractModel


class Seller(AbstractModel):
    user = models.OneToOneField('users.User', related_name='seller', verbose_name=_("User"))
    distance = models.IntegerField(verbose_name=_("Distance"))
    geoposition = GeopositionField(verbose_name=_("Geoposition"))

    titles = models.ManyToManyField('sellers.Title', blank=True, through='SellerTitle', verbose_name=_("Titles"))


    def __unicode__(self):
        return _(u"{user} is a seller.").format(user=self.user.get_full_name())


class Title(AbstractModel):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True, verbose_name=_("Title"))


    def __unicode__(self):
        return self.title


class SellerTitle(AbstractModel):
    seller = models.ForeignKey('sellers.Seller', verbose_name=_("User"))
    title = models.ForeignKey('sellers.Title', verbose_name=_("Title"))


    class Meta:
        ordering = ('seller', '-created_on',)
        unique_together = ('seller', 'title')


    def __unicode__(self):
        return _(u"{seller} is {title}").format(seller=self.seller.user.get_full_name(), title=self.title.title)