from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
    '',
    url('^static/(?P<path>.*?)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url('^$', 'entitlements.views.search_view', name='home_page'),
    url('^admin/', include(admin.site.urls)),
    url('^accounts/', include('registration.backends.default.urls')),
    url('^search/', include('entitlements.urls'))
    )
