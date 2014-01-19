from django.core.management.base import BaseCommand, CommandError
from engus.apps.dictionary.oxford_parser import parse
from engus.apps.dictionary.models import Word

class Command(BaseCommand):

    def handle(self, word, start_from=0, **options):
        words = Word.objects.filter(word__istartswith=word)[start_from:]
        words_count = words.count()
        saved_words = 0
        i = 0
        for word in words:
            i += 1
            print '\n----- Getting "%s" ----- (%d of %d (%d%%))' % (word, i, words_count, (float(i) / float(words_count) * 100))
            is_saved = parse(word.word)
            if is_saved: 
                saved_words += 1
                print 'Word saved (%d already)' % saved_words
