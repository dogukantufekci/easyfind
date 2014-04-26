from django.contrib import admin

from .models import Offer


class OfferAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, OfferAdmin)