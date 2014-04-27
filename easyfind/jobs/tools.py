import requests

import  zeropush
from zeropush.models import PushDevice

from django.conf import settings
from django.template.defaultfilters import timeuntil
from django.utils.translation import ugettext_lazy as _


from easyfind.decorators import async
from easyfind.tools import distance_in_kilometers

from sellers.models import Seller


@async
def zeropush_new_job(job):
    # Get sellers matching seller title
    sellers = Seller.objects.filter(titles=job.title).exclude(user=job.buyer).all()
    # Get sellers within distance
    suitable_sellers = []
    for seller in sellers:
        kwargs = {
            'lat1': float(job.geoposition.latitude),
            'long1': float(job.geoposition.longitude),
            'lat2': float(seller.geoposition.latitude),
            'long2': float(seller.geoposition.longitude),
        }
        if distance_in_kilometers(**kwargs) <= seller.distance:
            suitable_sellers.append(seller)
    # Get suitable user devices
    if len(suitable_sellers) > 0:
        devices = []
        for seller in suitable_sellers:
            devices += seller.user.pushdevice_set.all()
        # Notify devices
        if len(devices) > 0:
            if job.start_asap:
                alert = _(u"{title} ASAP").format(title=job.title.title)
            else:
                alert = _(u"{title} in {start_on}").format(title=job.title.title, start_on=timeuntil(job.start_on))
            print alert
            zeropush.notify_devices(devices, alert=alert)