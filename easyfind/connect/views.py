import json

from zeropush.models import PushDevice

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from users.models import User

from .tools import zeropush_register


@require_POST
@csrf_exempt
def paypal(request):
    # Check secret key
    secret_key = request.GET.get('secret_key')
    if not secret_key:
        response = {'error': 'Secret Key is missing.'}
        return HttpResponse(json.dumps(response), content_type="application/json")
    # Validate secret key
    if secret_key != settings.API_SECRET_KEY:
        response = {'error': 'Secret Key is not valid.'}
        return HttpResponse(json.dumps(response), content_type="application/json")

    paypal_id = request.POST.get('paypal_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    device_token = request.POST.get('device_token')

    # Check post data fiels
    if not (paypal_id and first_name and last_name and email and device_token):
        response = {'error': 'Missing key. paypal_id, first_name, last_name, email, and device_token are required.'}
        return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")

    # Check if user is registered
    user = authenticate(paypal_id=paypal_id)
    if user:

        # Check user active status
        if not user.is_active:
            response = {'error': 'User is not active.'}
            return HttpResponse(json.dumps(response), content_type="application/json")

        # Get or create iOS Device
        device, created = PushDevice.objects.get_or_create(token=device_token, user=user)
        if created:
            zeropush_register(device)

        # Respond
        response = {'data': {'user_id': user.id}}
        return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")

    # Create user
    username = "{0}{1}".format('paypal', paypal_id)
    # Add basic user data to dictionary
    kwargs = {
        'paypal_id': paypal_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'password': None,
    }
    # Create user
    user = User.objects.create_user(**kwargs)

    # Get or create iOS Device
    device, created = PushDevice.objects.get_or_create(token=device_token, user=user)
    if created:
        zeropush_register(device)
    
    # Respond
    response = {'data': {'user_id': user.id}}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


    