from django.test import TestCase
from fortytwoapps.models import Contact 


class ContactModelTestCase(TestCase):

    def setUp(self):

        self.contact = Contact.objects.create(

            name = 'Bhavneet',
            lastname = 'Singh',
            dateofdbirth = '1983-05-01',
            bio = 'Hello This is my bio', 
            email = 'bhavneetsi@gmail.com',
            jabber = 'bhavneetsi@42cc.co',
            skype = 'bhavneet.si',
            othercontacts='Other Contacts')
    
    def test_contact_basic(self):
        """
        Test for checking if correct values are inserted in db.
        """
        contact = Contact.objects.first()
        self.assertEqual(contact.name,'Bhavneet')
        self.assertEqual(contact.lastname,'Singh')
        self.assertEqual(contact.dateofdbirth,'1983-05-01')
        self.assertEqual(contact.bio,'Hello This is my bio')
        self.assertEqual(contact.email,'bhavneetsi@gmail.com')
        self.assertEqual(contact.jabber,'bhavneetsi@42cc.co')
        self.assertEqual(contact.skype,'bhavneet.si')
        self.assertEqual(contact.othercontacts,'Other Contacts')
