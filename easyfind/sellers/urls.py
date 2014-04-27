from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # titles
    url(r'^titles/$', 'sellers.views.titles', name='titles'),
)