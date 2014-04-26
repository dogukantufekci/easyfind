import datetime

from random import random
from hashlib import sha512

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone


def generate_key(length, extra=None):
    if length > 128:
        message = "Length must be less than or equal to 128"
        raise ValueError(message)
    return sha512(str(random())+str(extra)).hexdigest()[:length]


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