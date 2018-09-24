from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    help = 'prints all project models and the count of objects in every model.'

    def handle(self, *args, **options):
        self.stdout.write('Model name - Count of objects')
        for model in get_models():
            msg = '{} - {}'.format(model.__name__, model.objects.count())
            self.stdout.write(msg)
            self.stderr.write('Error: ' + msg)
