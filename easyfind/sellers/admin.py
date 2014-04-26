from django.contrib import admin

from .models import Seller


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seller, JobAdmin)