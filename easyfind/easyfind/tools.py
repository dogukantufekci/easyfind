import datetime

from random import random
from hashlib import sha512

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone


def generate_key(length, extra=None):
    if length > 128:
        message = "Length must be less than or equal to 128"
        raise ValueError(message)
    return sha512(str(random()) + str(extra)).hexdigest()[:length]


def generate_digit_key(length):
    if length > 12:
        message = "Length must be less than or equal to 12"
        raise ValueError(message)
    return str(random())[2:2+length]


def paginate(objects, limit, page):
    try:
        # make limit value integer
        # if value is 0 make it 10
        limit = int(limit) or 10
    except:
        limit = 10
    paginator = Paginator(objects, limit)
    try:
        page_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)
    return paginator, page_objects


def get_response(request, page_objects, data):
    # Response data
    response = {'data': data}
    # Response next
    if page_objects.has_next():
        next = "%s?" % request.path
        if request.GET.get('limit'):
            next += "limit=%s&" % request.GET['limit']
        if request.GET.get('secret_key'):
            next += "secret_key=%s&" % request.GET['secret_key']
        if request.GET.get('user_id'):
            next += "user_id=%s&" % request.GET['user_id']
        next += "page=%s" % page_objects.next_page_number()
        response.update({'next': next})
    else:
        response.update({'next': None})
    # Response previous
    if page_objects.has_previous():
        previous = "%s?" % request.path
        if request.GET.get('limit'):
            previous += "limit=%s&" % request.GET['limit']
        if request.GET.get('secret_key'):
            previous += "secret_key=%s&" % request.GET['secret_key']
        if request.GET.get('user_id'):
            previous += "user_id=%s&" % request.GET['user_id']
        previous += "page=%s" % page_objects.previous_page_number()
        response.update({'previous': previous})
    else:
        response.update({'previous': None})

    return response