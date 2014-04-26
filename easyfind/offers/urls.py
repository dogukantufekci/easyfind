from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # offers
    url(r'^$', 'offers.views.offers', name='offers'),
    
    # offer
    url(r'^(?P<offer_id>\d+)/$', 'offers.views.offer', name='offer'),
)