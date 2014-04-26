import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.template.defaultfilters import date as _date
from django.utils.timezone import localtime
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request
from easyfind.tools import get_response, paginate

from .models import Offer


@require_http_methods(['POST'])
@authenticate_request
def offers(request):
    pass


@require_http_methods(['GET'])
@authenticate_request
def offer(request, offer_id):
    pass