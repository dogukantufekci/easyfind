from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # home
    url(r'^$', 'lezizfirsat_vb.views.home', name='home'),
    # change language
    url(r'^change_language/$', 'lezizfirsat_vb.views.change_language', name='change_language'),

    # api
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
)

# Serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    
    import debug_toolbar
    
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )