from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from easyfind.tools import paginate

from .models import Deal


def home(request):
    return HttpResponseRedirect(reverse('deals:today'))


def today(request):
    # Get deals
    deals = Deal.objects.today()
    # Paginate deals
    paginator, page_deals = paginate(deals, 5, request.GET.get('page'))
    # Respond
    return render(request, 'deals/deals.html', {
        'title': _('Deals for Today'),
        'no_deal_message': _('Whoops. There is no today deal.'),
        'paginator': paginator,
        'deals': page_deals,
    })

    
def future(request):
    # Get deals
    deals = Deal.objects.future()
    # Paginate deals
    paginator, page_deals = paginate(deals, 5, request.GET.get('page'))
    # Respond
    return render(request, 'deals/deals.html', {
        'title': _('Future Deals'),
        'no_deal_message': _('Whoops. There is no future deal.'),
        'paginator': paginator,
        'deals': page_deals,
    })


def deal(request, year, month, day, slug, deal_id):
    # Get active deal or 404
    try:
        deal = Deal.objects.get(id=deal_id, is_active=True)
    except Deal.DoesNotExist:
        raise Http404
    # Respond
    return render(request, 'deals/deal.html', {
        'title': deal.get_short_title(),
        'deal': deal,
    })