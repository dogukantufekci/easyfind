from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # home
    url(r'^$', 'easyfind.views.home', name='home'),

    # django admin
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    
    import debug_toolbar
    
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )