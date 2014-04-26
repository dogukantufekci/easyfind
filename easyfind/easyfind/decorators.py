import json
import pytz

from threading import Thread

from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponseRedirect

from threading import Thread

from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone, translation

from users.models import User


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper


def authenticate_request(function):
    def wrap(request, *args, **kwargs):
        # Check if user is authenticated via session
        if request.user.is_authenticated():
            return function(request, *args, **kwargs)

        # Check secret key
        secret_key = request.GET.get('secret_key')
        if not secret_key:
            response = {'error': 'Secret Key is missing.'}
            return HttpResponse(json.dumps(response), content_type="application/json")
        # Validate secret key
        if secret_key != settings.API_SECRET_KEY:
            response = {'error': 'Secret Key is not valid.'}
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        # Check user id
        user_id = request.GET.get('user_id')
        if not user_id:
            response = {'error': 'User ID is missing.'}
            return HttpResponse(json.dumps(response), content_type="application/json")
        # Get user
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            response = {'error': 'User ID did not match any user.'}
            return HttpResponse(json.dumps(response), content_type="application/json")
        # Check user active status
        if not user.is_active:
            response = {'error': 'User is not active.'}
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        request.user = user
        timezone.activate(pytz.timezone(request.user.timezone))
        translation.activate(request.user.language)
        return function(request, *args, **kwargs)
    return wrap