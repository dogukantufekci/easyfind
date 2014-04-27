import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from easyfind.decorators import authenticate_request

from .models import Title


@require_http_methods(['GET'])
@authenticate_request
def titles(request):
    # Get titles
    titles = Title.objects.all()
    # Prepare data
    data = []
    for title in titles:
        data.append({
            'id': title.id,
            'title': title.title,
        })
    # Respond
    response = {'data': data}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=4, cls=DjangoJSONEncoder), content_type="application/json")