from django.contrib import admin

from .models import Seller, Title, SellerTitle


class SellerAdmin(admin.ModelAdmin):
    pass


class TitleAdmin(admin.ModelAdmin):
    pass


class SellerTitleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seller, SellerAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(SellerTitle, SellerTitleAdmin)