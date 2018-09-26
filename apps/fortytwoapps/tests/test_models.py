from django.test import TestCase
from fortytwoapps.models import Contact, Request
from datetime import datetime
from PIL import Image
from django.core.files import File
from django.conf import settings
import os
import glob


class ContactModelTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        imgfile = open("".
                       join([settings.BASE_DIR,
                            "/apps/fortytwoapps/tests/photos/test_img.png"]))
        self.contact = Contact.objects.create(
            name='test',
            lastname='user',
            dateofbirth='1983-05-01',
            bio='Hello This is my bio',
            email='bhavneetsi@gmail.com',
            jabber='bhavneetsi@42cc.co',
            skype='bhavneet.si',
            othercontacts='Other Contacts',
            photo=File(imgfile)
            )

    def tearDown(self):
        files = "".join([settings.BASE_DIR, "/uploads/photos/test_img*"])
        for file in glob.glob(files):
            os.remove(file)

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
        self.assertEqual(self.contact.photo.url,
                         '/uploads/photos/test_img.png')

    def test_image_size(self):
        """
        Test if size of stored image is as per size requirements of 200*200
        """
        required_photo_size = (200, 200)
        uploaded_photo_size = Image.open(self.contact.photo.path).size
        self.assertLessEqual(uploaded_photo_size, required_photo_size)


class RequestsModelTestCase(TestCase):
    """Test for RequestModel
    """
    def setUp(self):
            Request.objects.create(
                                   url='/',
                                   method='get',
                                   time=datetime.now().strftime(
                                                       '%Y-%m-%d %H:%M:%S'),
                                   viewed=False)

    def test_request_basic(self):
        """
        Test for Request model
        """
        self.request = Request.objects.first()
        self.assertEqual(self.request.url, '/')
        self.assertEqual(self.request.method, 'get')
        self.assertEqual(self.request.viewed, False)
