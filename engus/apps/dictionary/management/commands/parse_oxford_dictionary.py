from django.core.management.base import BaseCommand, CommandError
from engus.apps.dictionary.oxford_parser import parse

class Command(BaseCommand):

    def handle(self, *args, **options):
        for word in args:
            parse(word)
            self.stdout.write('Successfully parsed word "%s"' % word)
