from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       # register
                       url(r'^$', 'notifications.views.home', name='register'),


                       # login
                       #  url(r'^login/$', 'auth.views.login', name='login'),


                       # logout
                       # url(r'^logout/$', 'auth.views.logout', name='logout'),
                       # logout # after  # url(r'^logout/after/$', 'auth.views.logout_after', name='logout_after'),
)