from django.utils.translation import ugettext_lazy as _


class Statuses:
    WAITING = 0
    ACCEPTED = 1
    REJECTED = 2
    CHOICES = (
        (WAITING, _('Waiting')),
        (ACCEPTED, _('Accepted')),
        (REJECTED, _('Rejected')),
    )