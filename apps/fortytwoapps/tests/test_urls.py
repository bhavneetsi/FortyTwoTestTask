from django.test import TestCase
# Create your tests here.
from django.core.urlresolvers import resolve


class IndexUrlTestCase(TestCase):

    def test_root_url_for_index_view(self):
        """
        test if root of url uses index view

        """
        root = resolve('/')
        self.assertEqual(root.view_name, 'index')


class RequestUrlTestCase(TestCase):

    def test_request_url(self):
        """test for request url"""

        req = resolve('/requests/')
        self.assertEqual(req.view_name, 'requests')


class EditContactUrlTestCase(TestCase):

    def test_editcontact_url(self):
        """test for request url"""

        req = resolve('/updatecontact/')
        self.assertEqual(req.view_name, 'UpdateContact')