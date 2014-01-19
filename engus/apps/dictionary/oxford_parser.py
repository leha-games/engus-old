import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.text import slugify
from .models import Word, Definition, Example

DICTIONARY_BASE_URL = "http://oaadonline.oxfordlearnersdictionaries.com"
WORD_URL = DICTIONARY_BASE_URL + "/dictionary/"

def parse(word):
    url =  WORD_URL + word
    page = urllib.urlopen(url).read()
    soup = BeautifulSoup(page)
    word_not_found = soup.find(text=re.compile(r"(Sorry, no search result for)|(Entry not found in this dictionary)"))
    if word_not_found:
        is_deleted = delete_word(word, "not found in dictionary")
        return not is_deleted
    search_results = soup.find(id="relatedentries")
    word_anchors = search_results.find_all("a", href=re.compile(r"^{0}(_\d)?$".format(slugify(word))))
    if len(word_anchors) == 0:
        is_deleted = delete_word(word, "no word links")
        return not is_deleted
    for word_anchor in word_anchors:
        word_link = word_anchor["href"]
        parse_word(word_link, word)
    return True

def delete_word(word, message):
    try:
        word_obj = Word.objects.get(word=word)
        word_obj.delete()
        print 'Delete word "%s" since %s' % (word, message)
        with open('/var/webapps/engus/code/data/oxford_parsing_details/deleted_words.txt', 'a') as f:
            f.write("%s\n" % word)
        return True
    except Word.DoesNotExist:
        return False


def parse_word(word_link, origin_word):
    print 'Parsing "%s"' % word_link
    page = urllib.urlopen(WORD_URL + word_link).read()
    soup = BeautifulSoup(page)
    entry = soup.find("div", class_="entry")
    # remove idioms(ids-g), Vocabulary Building Boxes(unbox), phrasal verbs(pvp-g, pv-g), deriviates(dr-g):
    elements_to_remove = entry.find_all(["span", "div"], {"class": ["ids-g", "unbox", "pvp-g", "pv-g", "dr-g"]})
    if elements_to_remove:
        for el in elements_to_remove:
            el.decompose()
    get_word(entry, origin_word)


def get_word(element, origin_word):
    word = element.find("h2", class_="h").get_text().strip()
    if word != origin_word:
        print 'Word not the same: "%s" != "%s"' % (word, origin_word)
        with open('/var/webapps/engus/code/data/oxford_parsing_details/not-the-same-word.txt', 'a') as f:
            f.write('%s != %s\n' % (word, origin_word))
        return
    transcription_element = element.find("span", class_="phon-us")
    transcription = ''
    if transcription_element:
        transcription = transcription_element.get_text()
    audio_element = element.find("img", class_="sound")
    audio_url = None
    if audio_element:
        audio_rel_link = audio_element["onclick"].replace("playSoundFromFlash('", "").replace("', this)", "").strip()
        audio_url = DICTIONARY_BASE_URL + audio_rel_link
    part_of_speach_element = element.find("span", class_="pos") 
    if part_of_speach_element:
        part_of_speach = part_of_speach_element.get_text()
        is_oxford_3000_element = element.find("img", { "title": "Oxford3000" })
        is_oxford_3000 = False
        if is_oxford_3000_element:
            is_oxford_3000 = True
        word_obj = save_word(word, transcription, is_oxford_3000, audio_url)
        get_definitions(element, word_obj, part_of_speach)
    else:
        print "Not found part of speach"
        with open('/var/webapps/engus/code/data/oxford_parsing_details/not-found-part-of-speach.txt', 'a') as f:
            f.write('%s\n' % (word))


def get_definitions(element, word_obj, part_of_speach):
    definitions = element.find_all("span", class_="n-g") or (element, )
    for definition_element in definitions:
        get_definition(definition_element, word_obj, part_of_speach)


def get_definition(element, word_obj, part_of_speach):
    label = ''
    where_used = ''
    explanation = ''
    weight = 1
    weight_element = element.find("span", class_="z_n")
    if weight_element:
        weight = weight_element.get_text()
    text_element = element.find("span", { "class": ["d", "ud"] })
    if not text_element:
        return
    text = text_element.get_text()
    explanation_element = element.find("span", class_="dc")
    label_element = element.find("span", class_="label-g")
    if label_element:
        label = label_element.get_text().replace('(', '').replace(')', '').strip()
    where_used_element = element.find("span", class_="u")
    if where_used_element:
        where_used = list(where_used_element.stripped_strings)[1].strip()
    if explanation_element:
        explanation = explanation_element.get_text().strip()
    definition_obj = save_definition(word_obj, part_of_speach, text, weight, label, where_used, explanation)
    get_examples(element, definition_obj)


def get_examples(element, definition_obj):
    examples = element.find_all("span", class_="x")
    for example_element in examples:
        example_text_equal_element = example_element.find("span", class_="gl")
        example_text_equal = None
        if example_text_equal_element:
            example_text_equal = example_text_equal_element.get_text().replace("(=", "").replace(")", "").strip()
            example_text_equal_element.extract()
        example_text = example_element.get_text()
        example, example_created = Example.objects.get_or_create(
            definition=definition_obj,
            text=example_text,
        )
        if example_text_equal:
            example.text_equal = example_text_equal
        example.save()

def save_definition(word_obj, part_of_speach, text, weight, label, where_used, explanation):
    weight = int(weight)
    part_of_speach=getattr(Definition, part_of_speach.upper().replace(" ", ""))
    definition, definition_created = Definition.objects.get_or_create(
        word=word_obj, 
        part_of_speach=part_of_speach,
        weight=weight,
    )
    definition.definition = text
    definition.label = label
    definition.where_used = where_used
    definition.explanation = explanation
    definition.save()
    return definition

def save_word(word, transcription, is_oxford_3000, audio_url):
    word_obj, word_created = Word.objects.get_or_create(word=word)
    if word_created or word_obj.transcription == u'':
        word_obj.transcription = transcription
        if audio_url:
            audio_temp = NamedTemporaryFile(delete=True)
            audio_temp.write(urllib2.urlopen(audio_url).read())
            audio_temp.flush()
            word_obj.audio.save(word + ".mp3", File(audio_temp))
    word_obj.is_oxford_3000 = is_oxford_3000
    word_obj.save()
    return word_obj
