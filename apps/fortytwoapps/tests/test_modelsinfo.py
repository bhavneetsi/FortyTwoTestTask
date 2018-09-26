from StringIO import StringIO
from django.core.management import call_command
from django.test import TestCase


class TestModelsInfo(TestCase):

    def test_models_info(self):
        """test for modelsinfo command
        """
        out = StringIO()
        error = StringIO()
        call_command('modelsinfo', stdout=out, stderr=error)
        self.assertIn('Model name - Count of objects', out.getvalue())
        self.assertIn('User', out.getvalue())
        self.assertIn('Error: User', error.getvalue())
