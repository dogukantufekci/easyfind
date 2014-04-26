import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.template.defaultfilters import date as _date
from django.utils.timezone import localtime
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request
from easyfind.tools import get_response, paginate

from .models import Job


@require_http_methods(['GET', 'POST'])
@authenticate_request
def jobs(request):
    if request.method == 'GET':
        # Get jobs
        jobs = Job.objects.filter(buyer=request.user)
        # Paginate jobs
        paginator, page_objects = paginate(jobs, request.GET.get('limit'), request.GET.get('page'))
        # Prepare data
        data = []
        for page_object in page_objects:
            data.append({
                'id': page_object.id,
                'buyer': {
                    'id': page_object.buyer.id,
                    'name': page_object.buyer.get_full_name(),
                },
                'title': {
                    'id': page_object.title.id,
                    'title': page_object.title.title,
                },
                'geoposition': {
                    'latitude': page_object.geoposition.latitude,
                    'longitude': page_object.geoposition.longitude,
                },
                'start_on': _date(localtime(page_object.start_on)),
                'start_asap': page_object.start_asap,
            })
        # Respond
        response = get_response(request, page_objects, data)
    
    elif request.method == 'POST':
        pass

    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


@require_http_methods(['GET'])
@authenticate_request
def offer(request, offer_id):
    pass


@require_http_methods(['GET'])
@authenticate_request
def job_offers(request, offer_id):
    pass