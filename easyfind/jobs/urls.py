from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # jobs
    url(r'^$', 'jobs.views.jobs', name='jobs'),
    
    # job
    url(r'^(?P<job_id>\d+)/$', 'jobs.views.job', name='job'),
    # job # offers
    url(r'^(?P<job_id>\d+)/offers/$', 'jobs.views.job_offers', name='job_offers'),
)