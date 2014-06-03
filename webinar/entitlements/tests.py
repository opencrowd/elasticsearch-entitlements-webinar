# 2014.06.03 13:21:05 EDT
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from views import do_search
from models import create_initial_db, create_initial_es

class SearchTest(TestCase):

    def setUp(self):
        create_initial_db()
        create_initial_es()



    def get_user(self, uid):
        return User.objects.get(entitlement_profile__entitlement_user__uid=uid)




class SearchFunctionTest(SearchTest):

    def perform_search(self, uid):
        return do_search(self.get_user(uid), '')



    def test_search_D00001(self):
        """
        Balance field not masked for 'Universal Widget' or 'John Smith'
        Balance field masked for 2 accounts, 'Acme Widgets' and 'Jane Doe'
        """
        (count, results, facets,) = self.perform_search('D00001')
        self.assertEquals(count, 4)
        self.assertEquals(facets['balance_stats']['total'], 2235872)
        for result in results:
            if result['balance'] == '****':
                self.assertTrue(result['name'] == 'Acme Widgets' or result['name'] == 'Jane Doe')
            else:
                self.assertTrue(result['name'] == 'Universal Widget' or result['name'] == 'John Smith')




    def test_search_D00002(self):
        """
        Balance field not masked for 'Acme Widgets'
        Balance field masked for all other accounts.
        """
        (count, results, facets,) = self.perform_search('D00002')
        self.assertEquals(count, 4)
        self.assertEquals(facets['balance_stats']['total'], 2235872)
        for result in results:
            if result['balance'] == '****':
                self.assertNotEquals(result['name'], 'Amce Widgets')
            else:
                self.assertEquals(result['name'], 'Acme Widgets')




    def test_search_D00003(self):
        """
        This user can fully see 1 account, for customer 'Jane Doe'.
        Balance field is masked for 2nd account, for customer 'John Smith'.
        """
        (count, results, facets,) = self.perform_search('D00003')
        self.assertEquals(count, 2)
        self.assertEquals(facets['balance_stats']['total'], 100.5)
        for result in results:
            if 'C00001' in result['groups'] or 'D00003' in result['coverage']:
                self.assertNotEquals(result['balance'], '****')
                self.assertEquals(result['name'], 'Jane Doe')
            else:
                self.assertEquals(result['balance'], '****')
                self.assertEquals(result['name'], 'John Smith')




    def test_search_D00004(self):
        """
        Balance field is masked for both accounts
        """
        (count, results, facets,) = self.perform_search('D00004')
        self.assertEquals(count, 2)
        self.assertEquals(facets['balance_stats']['total'], 0.0)
        for result in results:
            self.assertEquals(result['balance'], '****')





class ViewTests(SearchTest):

    def login_as(self, uid):
        user = self.get_user(uid)
        client = Client()
        client.login(username=user.username, password='test123')
        return client



    def test_view_D00001(self):
        client = self.login_as('D00001')
        response = client.get(reverse('search_view'))
        self.assertEquals(response.status_code, 200)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.06.03 13:21:05 EDT
