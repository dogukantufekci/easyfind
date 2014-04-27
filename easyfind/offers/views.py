import json

from geoposition.forms import Geoposition

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request

from sellers.models import Seller

from .forms import OfferForm
from .models import Offer


@require_http_methods(['GET', 'POST'])
@csrf_exempt
@authenticate_request
def offers(request):
    try:
        request.user.seller
    except Seller.DoesNotExist:
        response = {'error': 'User is not a seller.'}
        return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")

    if request.method == 'GET':
        # Get offers
        offers = Offer.objects.filter(seller=request.user)
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
    
    elif request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            # Create offer
            offer = form.save(commit=False)
            offer.seller = request.user.seller
            
            if Offer.objects.filter(job=offer.job, seller=offer.seller).count() > 0:
                response = {'error': 'Seller has already made an offer for this job.'}
            else:
                offer.save()
                # Return with created offer as response
                response = {
                    'data': {
                        'id': offer.id,
                        'job_id': offer.job.id,
                        'seller': {
                            'id': offer.seller.user.id,
                            'name': offer.seller.user.get_full_name(),
                        },
                        'price': offer.price,
                        'status': offer.status,
                    },
                }
        else:
            response = {'error': 'Form data is not valid.'}

    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


@require_http_methods(['GET'])
@authenticate_request
def offer(request, offer_id):
    # Get offer or 404
    try:
        offer = Offer.objects.get(id=offer_id)
    except Offer.DoesNotExist:
        raise Http404
    # Respond
    response = {
        'data': {
            'id': offer.id,
            'job_id': offer.job.id,
            'seller': {
                'id': offer.seller.user.id,
                'name': offer.seller.user.get_full_name(),
            },
            'price': offer.price,
            'status': offer.status,
        },
    }
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")