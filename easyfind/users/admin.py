from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'birthday', 'gender', 'language', 'timezone', 'is_staff', 'is_active', 'username', 'email', 'password', 'created_on', 'updated_on', 'last_login',)
    readonly_fields = ('password', 'created_on', 'updated_on', 'last_login',)


admin.site.register(User, UserAdmin)


from django.contrib.auth.models import Group
from django.contrib.sites.models import Site


admin.site.unregister(Group)
admin.site.unregister(Site)