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
        if gender.lower() == 'male':
            return Genders.MALE
        elif gender.lower() == 'female':
            return Genders.FEMALE
        return


class Timezones:
    CHOICES = (
        ('UTC', _('(+00:00) UTC')),
        ('Europe/London', _('(+00:00) Europe/London ')),
        ('Europe/Istanbul', _('(+02:00) Europe/Istanbul ')),
        ('Asia/Nicosia', _('(+02:00) Asia/Nicosia')),
    )