from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _



def home(request):
    return HttpResponse('Hello world!!!!')


