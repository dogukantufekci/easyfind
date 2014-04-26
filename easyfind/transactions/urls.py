from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # transactions
    url(r'^$', 'transactions.views.transactions', name='transactions'),
)