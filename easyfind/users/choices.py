from django.utils.translation import ugettext_lazy as _


class Genders:
    FEMALE = 1
    MALE = 2
    CHOICES = (
        (FEMALE, _('Female')),
        (MALE, _('Male')),
    )

    @staticmethod
    def get_value(gender):
        gender = gender.lower()
        if gender == 'male' or gender == 'm':
            return Genders.MALE
        if gender == 'female' or gender == 'f':
            return Genders.FEMALE


class Timezones:
    CHOICES = (
        ('UTC', _('(+00:00) UTC')),
        ('Europe/London', _('(+00:00) Europe/London ')),
        ('Europe/Istanbul', _('(+02:00) Europe/Istanbul ')),
        ('Asia/Nicosia', _('(+02:00) Asia/Nicosia')),
    )