from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^paypal/$', 'connect.views.paypal', name='paypal'),
)