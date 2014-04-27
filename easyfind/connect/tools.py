import requests

from django.conf import settings

from easyfind.decorators import async


@async
def zeropush_register(device):
    r = requests.post('https://api.zeropush.com/register', {
        'auth_token': settings.ZEROPUSH_AUTH_TOKEN,
        'device_token': device.token,
    })
    if r.text != '{"message":"ok"}':
        device.delete()