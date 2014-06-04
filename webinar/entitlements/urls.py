from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
    'entitlements.views',
    url('^search/(?P<uid>.*?)$', 'search_view', name='search_view')
    )

