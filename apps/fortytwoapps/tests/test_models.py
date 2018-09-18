from django.test import TestCase
from fortytwoapps.models import Contact


class ContactModelTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        self.contact = Contact.objects.create(

            name='test',
            lastname='user',
            dateofbirth='1983-05-01',
            bio='Hello This is my bio',
            email='bhavneetsi@gmail.com',
            jabber='bhavneetsi@42cc.co',
            skype='bhavneet.si',
            othercontacts='Other Contacts')

    def test_contact_basic(self):
        """
        Test for checking if correct values are inserted in db.
        """
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'test')
        self.assertEqual(contact.lastname, 'user')
        self.assertEqual(contact.dateofbirth.strftime('%Y-%m-%d'),
                         '1983-05-01')
        self.assertEqual(contact.bio, 'Hello This is my bio')
        self.assertEqual(contact.email, 'bhavneetsi@gmail.com')
        self.assertEqual(contact.jabber, 'bhavneetsi@42cc.co')
        self.assertEqual(contact.skype, 'bhavneet.si')
        self.assertEqual(contact.othercontacts, 'Other Contacts')


class RequestsModelTestCase(TestCase):
    """Test for RequestModel
    """
    def setUp(self):
            Request.objects.create(
                                   url='/',
                                   method='get',
                                   time=fuzzy.FuzzyDate(date.today()),
                                   viewed=False)

    def test_request_basic(self):
        """
        Test for Request model
        """
        self.request = Request.objects.first()
        self.assertEqual(self.request.url, '/')
        self.assertEqual(self.request.method, 'get')
        self.assertEqual(self.request.viewed, False)
