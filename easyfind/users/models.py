from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from .choices import Genders, Timezones


class UserManager(BaseUserManager):
    
    def create_user(self, username, password=None, **extra_fields):
        # Check for username
        if not username:
            raise ValueError(_('Username is a required field.'))
        if not User.is_unique_username(username):
            raise ValueError(_('Username must be unique.'))
        # Get user model instance
        user = self.model(username=username, **extra_fields)
        # Set user active
        user.is_active = True
        # Set hashed password
        user.set_password(password)
        # Save user
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        # Create user
        user = self.create_user(username, password, **extra_fields)
        # Set user staff
        user.is_staff = True
        # Set user active
        user.is_active = True
        # Set user superuser
        user.is_superuser = True
        # Save user
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    NAME_MAX_LENGTH = 30
    USERNAME_MAX_LENGTH = 30
    EMAIL_MAX_LENGTH = 255
    LANGUAGE_MAX_LENGTH = 5
    TIMEZONE_MAX_LENGTH = 32

    created_on = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("Created on"))
    updated_on = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Updated on"))

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True, verbose_name=_("Username"))
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH, unique=True, verbose_name=_("Email"))
    
    first_name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name=_("First name"))
    last_name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name=_("Last name"))

    birthday = models.DateField(blank=True, null=True, verbose_name=_("Birthday"))
    gender = models.IntegerField(blank=True, choices=Genders.CHOICES, null=True, verbose_name=_("Gender"))

    language = models.CharField(choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, max_length=LANGUAGE_MAX_LENGTH, verbose_name=_("Language"))
    timezone = models.CharField(choices=Timezones.CHOICES, default=settings.TIME_ZONE, max_length=TIMEZONE_MAX_LENGTH, verbose_name=_("Timezone"))

    # admin
    is_staff = models.BooleanField(default=False, verbose_name=_("Is staff"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is active"))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name',) # required for superuser creation

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __unicode__(self):
        return self.get_full_name()

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)