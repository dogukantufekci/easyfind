import json

import pymongo

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request


client = pymongo.MongoClient(settings.MONGO_URI)
db = client.get_default_database()


@require_http_methods(['GET')
@authenticate_request
def notifications(request):
    # Get jobs
    notifications = db.notifications.find({})
    # Respond
    response = {'data': notifications}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")