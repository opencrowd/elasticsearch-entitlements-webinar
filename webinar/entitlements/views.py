# 2014.06.03 13:21:05 EDT
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import OrderedDict
import requests
import json
from models import EntitlementProfile
from forms import SearchForm
import pprint
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
SEARCH_URL = 'http://localhost:9200/webinar/_search'

def do_search(user, query_string):
    try:
        if isinstance(user, basestring):
            profile = EntitlementProfile.objects.select_related().get(entitlement_user__uid=user)
        else:
            profile = EntitlementProfile.objects.select_related().get(user=user)
    except EntitlementProfile.DoesNotExist:
        profile = None
    if profile:
        uid = profile.entitlement_user.uid
        gid = profile.entitlement_group.gid
        base_query = OrderedDict()
        base_query['filter'] = {'or': [{'term': {'coverage': uid}},
                {'term': {'groups': gid}},
                {'term': {'restricted': gid}},
                {'term': {'unrestricted': gid}}]}
        base_query['query'] = {'match_all': {}}
        base_query['script_fields'] = {'balance': {'params': {'gid': gid,
                                'uid': uid},
                     'script': '((doc[\'coverage\'].value.contains(uid))) ? doc[\'balance\'].value : "****"'}}
        base_query['fields'] = ['name',
         'coverage',
         'groups',
         'account_type']
        base_query['sort'] = ['account_type']
        base_query['facets'] = {'balance_stats': {'statistical': {'params': {'gid': gid,
                                                      'uid': uid},
                                           'script': "((doc['coverage'].value.contains(uid)) || doc['unrestricted'].value.contains(gid)) ? doc['balance'].value : 0"}}}
    else:
        base_query = OrderedDict()
        base_query['query'] = {'match_all': {}}
        base_query['script_fields'] = {'balance': {'script': "doc['balance'].value"}}
        base_query['fields'] = ['name',
         'coverage',
         'groups',
         'account_type']
        base_query['sort'] = ['account_type']
        base_query['facets'] = {'balance_stats': {'statistical': {'field': 'balance'}}}
    if query_string:
        base_query['query'] = {'query_string': {'query': query_string}}
    r = requests.post(SEARCH_URL, data=json.dumps(base_query))
    r.raise_for_status()
    js = r.json()
    return (base_query,
     js['hits']['total'],
     (x.get('_source', x.get('fields')) for x in js['hits']['hits']),
     js['facets'])



@login_required
def search_view(request, uid):
    form = SearchForm(request.GET)
    if form.is_valid():
        (query, count, results, facets,) = do_search(uid, form.cleaned_data['query'])
    else:
        (query, count, results, facets,) = do_search(uid, '')
    sio = StringIO.StringIO()
    pprint.pprint(query, stream=sio, indent=4)
    context = {'query': json.dumps(query, indent=4),
     'count': count,
     'results': results,
     'facets': facets}
    return render(request, 'entitlements/search.html', context)



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.06.03 13:21:05 EDT
