import pymongo

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

client = pymongo.MongoClient(settings.MONGO_URI)

db = client.get_default_database()


def home(request):
    db.notifications.insert({'asdf': 'india2'})
    result = db.notifications.find({'asdf': 'india2'})
    return HttpResponse(result[0]['asdf'])