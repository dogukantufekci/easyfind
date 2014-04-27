import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request

import paypalrestsdk
from paypalrestsdk import Payment

from django.conf import settings
from django.http import HttpResponse


@require_http_methods(['GET'])
@authenticate_request
def paypal_buy(request):
    paypalrestsdk.configure({
        "mode": settings.PAYPAL_MODE,
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET})

    payment = Payment({
        "intent": "sale",

        # ###Payer
        # A resource representing a Payer that funds a payment
        # Payment Method as 'paypal'
        "payer": {
            "payment_method": "paypal"
        },

        # ###Redirect URLs
        "redirect_urls": {
            "return_url": settings.PAYPAL_RETURN_URL,
            "cancel_url": settings.PAYPAL_CANCEL_URL,
        },

        # ###Transaction
        # A transaction defines the contract of a
        # payment - what is the payment for and who
        # is fulfilling it.
        "transactions": [{

                             # ### ItemList
                             "item_list": {
                                 "items": [{
                                               "name": "item",
                                               "sku": "item",
                                               "price": "0.10",
                                               "currency": "USD",
                                               "quantity": 1}]},

                             # ###Amount
                             # Let's you specify a payment amount.
                             "amount": {
                                 "total": "0.10",
                                 "currency": "USD"},
                             "description": "This is the payment transaction description......"}]})

    # Create Payment and return status
    if payment.create():
        response = {'data': {'url': payment.links[1]}}
    else:
        response = {'error': 'Something went wrong.'}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")

@require_http_methods(['GET'])
@authenticate_request
def paypal_cancel(request):
    # Respond
    response = {'data': {'url': }}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


@require_http_methods(['GET'])
@authenticate_request
def paypal_return(request):
    # Respond
    response = {'data': {'url': }}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")