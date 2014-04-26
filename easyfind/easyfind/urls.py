from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    # home
    url(r'^$', 'easyfind.views.home', name='home'),

    url(r'^api/connect/', include('connect.urls', namespace='connect', app_name='connect')),
    url(r'^api/jobs/', include('jobs.urls', namespace='jobs', app_name='jobs')),
    url(r'^api/notifications/', include('notifications.urls', namespace='notifications', app_name='notifications')),
    url(r'^api/offers/', include('offers.urls', namespace='offers', app_name='offers')),

    # django admin
    url(r'^admin/', include(admin.site.urls))
)

# Serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )