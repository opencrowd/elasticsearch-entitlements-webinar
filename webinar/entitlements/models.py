from django.db import models
from django.contrib.auth.models import User
import json
import requests

class EntitlementGroup(models.Model):
    gid = models.CharField(max_length=10)


class EntitlementUser(models.Model):
    uid = models.CharField(max_length=10)


class EntitlementProfile(models.Model):
    user = models.OneToOneField(User, related_name='entitlement_profile')
    entitlement_group = models.ForeignKey(EntitlementGroup, null=True)
    entitlement_user = models.ForeignKey(EntitlementUser, null=True)


def create_initial_db():
    _ = [ x.user.delete() for x in EntitlementProfile.objects.all() ]
    user = User.objects.create_user(username='uncontrolled')
    EntitlementProfile.objects.create(user=user)
    e_group = EntitlementGroup.objects.create(gid='C00001')
    user = User.objects.create_user(username='corporate1')
    e_user = EntitlementUser.objects.create(uid='D00001')
    EntitlementProfile.objects.create(user=user, entitlement_group=e_group, entitlement_user=e_user)
    user = User.objects.create_user(username='corporate2')
    e_user = EntitlementUser.objects.create(uid='D00002')
    EntitlementProfile.objects.create(user=user, entitlement_group=e_group, entitlement_user=e_user)
    e_group = EntitlementGroup.objects.create(gid='C00002')
    user = User.objects.create_user(username='retail1')
    e_user = EntitlementUser.objects.create(uid='D00003')
    EntitlementProfile.objects.create(user=user, entitlement_group=e_group, entitlement_user=e_user)
    user = User.objects.create_user(username='retail2')
    e_user = EntitlementUser.objects.create(uid='D00004')
    EntitlementProfile.objects.create(user=user, entitlement_group=e_group, entitlement_user=e_user)
    for user in User.objects.all():
        user.set_password('test123')
        user.save()




def create_initial_es():
    d = {'number_of_replicas': 0,
     'number_of_shards': 1}
    r = requests.put('http://localhost:9200/webinar/', data=json.dumps(d))
    d = {'account': {'properties': {'restricted_fields': {'index': 'not_analyzed',
                                                      'type': 'string'},
                                'account_type': {'index': 'not_analyzed',
                                                 'type': 'string'},
                                'name': {'type': 'string',
                                         'analyzer': 'standard'},
                                'groups': {'index': 'not_analyzed',
                                           'type': 'string'},
                                'coverage': {'index': 'not_analyzed',
                                             'type': 'string'},
                                'restricted': {'index': 'not_analyzed',
                                               'type': 'string'},
                                'unrestricted': {'index': 'not_analyzed',
                                                 'type': 'string'},
                                'balance': {'type': 'float'}}}}
    r = requests.post('http://localhost:9200/webinar/account/_mapping', data=json.dumps(d))
    d1 = {'restricted_fields': ['balance'],
     'account_type': 'CORPORATE',
     'name': 'Universal Widget',
     'groups': ['C00001'],
     'coverage': ['D00001'],
     'restricted': ['C00001'],
     'unrestricted': ['C00001'],
     'balance': 1000000}
    op1 = {'index': {'_index': 'webinar',
               '_type': 'account',
               '_id': 0}}
    d2 = {'restricted_fields': ['balance'],
     'account_type': 'CORPORATE',
     'name': 'Acme Widgets',
     'groups': ['C00001'],
     'coverage': ['D00002'],
     'restricted': ['C00001'],
     'unrestricted': ['C00001'],
     'balance': 1234567}
    op2 = {'index': {'_index': 'webinar',
               '_type': 'account',
               '_id': 1}}
    d3 = {'restricted_fields': ['balance'],
     'account_type': 'CONSUMER',
     'name': 'Jane Doe',
     'groups': ['C00002'],
     'coverage': ['D00003'],
     'restricted': ['C00002'],
     'unrestricted': ['C00001'],
     'balance': 100.5}
    op3 = {'index': {'_index': 'webinar',
               '_type': 'account',
               '_id': 2}}
    d4 = {'restricted_fields': ['balance'],
     'account_type': 'CONSUMER',
     'name': 'John Smith',
     'groups': ['C00002'],
     'coverage': ['D00001'],
     'restricted': ['C00002'],
     'unrestricted': ['C00001'],
     'balance': 1204.5}
    op4 = {'index': {'_index': 'webinar',
               '_type': 'account',
               '_id': 3}}
    bulk_request = '\n'.join((json.dumps(x) for x in (op1,
     d1,
     op2,
     d2,
     op3,
     d3,
     op4,
     d4)))
    bulk_request = bulk_request + '\n'
    r = requests.post('http://localhost:9200/_bulk', data=bulk_request)

