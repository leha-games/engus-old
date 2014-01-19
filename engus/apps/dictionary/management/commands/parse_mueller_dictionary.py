from django.core.management.base import BaseCommand, CommandError
from engus.apps.dictionary.mueller_parser import parse_dictionary

class Command(BaseCommand):

    def handle(self, *args, **options):
        parse_dictionary(args[0])
        self.stdout.write('Successfully parsed mueller dictionary')