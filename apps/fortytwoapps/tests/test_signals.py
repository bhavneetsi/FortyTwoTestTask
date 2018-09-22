from django.test import TestCase
from fortytwoapps.models import Contact, ObjectLog

class TestSignals(TestCase):

    def setUp(self):
        Contact.object.create(name='test',
                              lastname='user',
                              dateofbirth='1983-05-01',
                              bio='none',
                              email='test@test.com',
                              jabber='test@42cc.co',
                              skype='test.test',
                              othercontacts='no')
        self.contact = Contact.objects.last()

    def test_create_post_save_signal(self):
        """
        Test post Save signal for create is creating log in db
        """
        objectlog = ObjectLog.objects.last()
        self.assertsEqual(objectlog.appname, 'fortytwoapps')
        self.assertsEqual(objectlog.objectname, 'Contact')
        self.assertsEqual(objectlog.action, 'created')

    def test_update_post_save_signal(self):
        """
        Test post Save signal for update is creating log in db
        """
        self.contact.name = 'new_test'
        self.contact.save()
        objectlog = ObjectLog.objects.last()
        self.assertsEqual(objectlog.appname, 'fortytwoapps')
        self.assertsEqual(objectlog.objectname, 'Contact')
        self.assertsEqual(objectlog.action, 'updated')

    def test_delete_post_save_signal(self):
        """
        Test post Save signal for delete is creating log in db
        """
        self.contact.delete()
        objectlog = ObjectLog.objects.last()
        self.assertsEqual(objectlog.appname, 'fortytwoapps')
        self.assertsEqual(objectlog.objectname, 'Contact')
        self.assertsEqual(objectlog.action, 'deleted')
