# 2014.06.03 13:21:05 EDT
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
    'entitlements.views',
    url('^search/(?P<uid>.*?)$', 'search_view', name='search_view')
    )

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.06.03 13:21:05 EDT
