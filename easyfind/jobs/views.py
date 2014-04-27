import json

from geoposition.forms import Geoposition

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request

from .forms import JobForm
from .models import Job


@require_http_methods(['GET', 'POST'])
@csrf_exempt
@authenticate_request
def jobs(request):
    if request.method == 'GET':
        # Get jobs
        jobs = Job.objects.filter(buyer=request.user)
        # Prepare data
        data = []
        for job in jobs:
            data.append({
                'id': job.id,
                'buyer': {
                    'id': job.buyer.id,
                    'name': job.buyer.get_full_name(),
                },
                'title': {
                    'id': job.title.id,
                    'title': job.title.title,
                },
                'geoposition': {
                    'latitude': job.geoposition.latitude,
                    'longitude': job.geoposition.longitude,
                },
                'start_on': localtime(job.start_on),
                'start_asap': job.start_asap,
                'is_active': job.is_active,
            })
        # Respond
        response = {'data': data}
    
    elif request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Create job
            job = form.save(commit=False)
            job.buyer = request.user
            job.start_on = timezone.now()
            job.geoposition = Geoposition(form.cleaned_data['geoposition_0'], form.cleaned_data['geoposition_1'])
            job.save()
            # Return with created job as response
            response = {
                'data': {
                    'id': job.id,
                    'buyer': {
                        'id': job.buyer.id,
                        'name': job.buyer.get_full_name(),
                    },
                    'title': {
                        'id': job.title.id,
                        'title': job.title.title,
                    },
                    'geoposition': {
                        'latitude': job.geoposition.latitude,
                        'longitude': job.geoposition.longitude,
                    },
                    'start_on': localtime(job.start_on),
                    'start_asap': job.start_asap,
                    'is_active': job.is_active,
                },
            }
        else:
            response = {'error': 'Form data is not valid.'}

    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


@require_http_methods(['GET'])
@authenticate_request
def job(request, job_id):
    # Get job or 404
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404
    # Respond
    response = {'data': {
        'id': job.id,
        'buyer': {
            'id': job.buyer.id,
            'name': job.buyer.get_full_name(),
        },
        'title': {
            'id': job.title.id,
            'title': job.title.title,
        },
        'geoposition': {
            'latitude': job.geoposition.latitude,
            'longitude': job.geoposition.longitude,
        },
        'start_on': localtime(job.start_on),
        'start_asap': job.start_asap,
        'is_active': job.is_active,
    }}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


@require_http_methods(['GET'])
@authenticate_request
def job_offers(request, job_id):
    # Get job or 404
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404
    # Get offers
    offers = job.offers.all()
    # Prepare data
    data = []
    for offer in offers:
        data.append({
            'id': offer.id,
            'job_id': offer.job.id,
            'seller': {
                'id': offer.seller.user.id,
                'name': offer.seller.user.get_full_name(),
            },
            'price': offer.price,
            'status': offer.status,
        })
    # Respond
    response = {'data': data}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")