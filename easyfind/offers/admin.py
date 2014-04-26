from django.contrib import admin

from models import Offer


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, JobAdmin)