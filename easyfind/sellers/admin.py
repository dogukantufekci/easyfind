from django.contrib import admin

from .models import Seller


class SellerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seller, SellerAdmin)