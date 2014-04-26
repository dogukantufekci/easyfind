from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # notifications
    url(r'^$', 'notifications.views.notifications', name='notifications'),
)