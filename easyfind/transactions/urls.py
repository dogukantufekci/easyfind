from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # buy
    url(r'^buy/$', 'transactions.views.buy', name='buy'),
)