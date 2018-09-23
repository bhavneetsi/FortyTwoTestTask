from django.test import TestCase
from fortytwoapps.models import Contact
from django.core.urlresolvers import reverse
from django.template import Template, Context, TemplateSyntaxError


class TestEditLinkTag(TestCase):
    TEMPLATE = Template('{% load edit_link_tag %} \
                        {% edit_link contact contact.pk %}')

    def test_link_on_index(self):
        """
        Test on index page custom link renders to edit contact on admin
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, '/admin/fortytwoapps/contact/1/')

    def test_edit_link_wrong_object(self):
        """
        Test edit_link tag raises error in case wrong object is passed
        """
        with self.assertRaises(TemplateSyntaxError):
            self.TEMPLATE.render(Context({'contact': "none"}))

    def test_edit_link_correct_object(self):
        """
        Test edit_link tag with correct object should have correct
        admin page link
        """
        contact = Contact.objects.first()
        rendered = self.TEMPLATE.render(Context({'contact': contact}))
        self.assertIn('admin/fortytwoapps/contact/1/', rendered)
