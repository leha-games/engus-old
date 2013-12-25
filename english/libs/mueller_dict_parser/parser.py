# coding: utf-8
import re
import io
from english.apps.dictionary.models import Word


def transcription_decode(string):
    mapping = [
        (u'Q', u"æ"),
        (u'W', u"ʷ"),
        (u'A', u"ɑ"),
        (u'Ы', u":"),
        (u'╚', u"ə"),
        (u'E', u"ɛ"),
        (u'█', u"ɔ"),
        (u'ц', u"ʌ"),
        (u'I', u"ɪ"),
        (u'х', u"ˈ"),
        (u'г', u"ˌ"),
        (u'H', u"ʰ"),
        (u'Z', u"ʒ"),
        (u'N', u"ŋ"),
        (u'S', u"ʃ"),
        (u'D', u"ð"),
        (u'T', u"θ"), 
    ]
    for k, v in mapping:
        string = string.replace(k, v)
    return string

def transcr_repl(matchobj):
    return transcription_decode(matchobj.group(0))

def get_word_and_translation(line):
    # Two blank symbols separate an English word from its translation
    splitted = line.split('  ')
    word = splitted[0]
    translation = '  '.join(splitted[1:]).strip() 
    return (word, translation)

transcription_pattern = r'\[(.*?)\]'

def get_transcription(line):
    decoded_first_transcription = '' 
    matchobj = re.search(transcription_pattern, line)
    if matchobj:
        decoded_first_transcription = transcription_decode(matchobj.group(0))
        return decoded_first_transcription

def transcription_replace(string):
    return re.sub(transcription_pattern, transcr_repl, string)

def remove_transcriptions(line):
    return re.sub(transcription_pattern, '', line)

def first_level_delimeter_repl(matchobj):
    if matchobj.group(1) and matchobj.group(2):
        return '\n%s)' % matchobj.group(2)
    else:
        return matchobj.group(0)
    
def first_level_delimeter(string):
    delimeters_pattern = r'(_)(M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))'
    return re.sub(delimeters_pattern, first_level_delimeter_repl, string)

def second_level_delimeter_repl(matchobj):
    if matchobj.group(1):
        return '\n\t%s.' % matchobj.group(1)

def second_level_delimeter(string):
    delimeter_pattern = r'(\d+)\.'
    return re.sub(delimeter_pattern, second_level_delimeter_repl, string)

def third_level_delimeter_repl(matchobj):
    if matchobj.group(1):
        return '\n\t\t%s)' % matchobj.group(1)

def third_level_delimeter(string):
    delimeter_pattern = r'(\d+)>'
    return re.sub(delimeter_pattern, third_level_delimeter_repl, string)

def fourth_level_delimeter_repl(matchobj):
    if matchobj.group(1):
        return '\n\t\t\t%s)' % matchobj.group(1)

def fourth_level_delimeter(string):
    delimeter_pattern = r'(.)>'
    return re.sub(delimeter_pattern, fourth_level_delimeter_repl, string)

def fill_models(word, transcription, translation):
    word_object, created = Word.objects.get_or_create(word=word)
    if transcription:
        word_object.transcription = transcription
    if not created:
        if word_object.mueller_definition != translation:
            word_object.mueller_definition += '\n\n' + translation
    else:
        word_object.mueller_definition = translation
    word_object.save()

def parse_dictionary(filepath):
    with open(filepath, 'r') as mueller:
        for line in mueller:
            # Each line represents a word with translation
            line = unicode(line, 'koi8-r')
            word, translation = get_word_and_translation(line)
            transcription = get_transcription(translation)
            translation = remove_transcriptions(translation)
            #translation = transcription_replace(translation)
            translation = first_level_delimeter(translation)
            translation = second_level_delimeter(translation)
            translation = third_level_delimeter(translation)
            #translation = fourth_level_delimeter(translation)
            #translation = translation.strip('\n')
            # Fill Django models
            fill_models(word, transcription, translation)
