# -*- coding: utf-8 -*-
import collections
import re
from engus.apps.dictionary.models import Word
from .models import MaterialWord


def strip_suffixes(word):
    return re.sub('(es|s|ies|ing|ed|er|est|ly)$', '', word)


def strip_non_characters(word):
    return re.sub("[^a-zA-Z]+", "", word)


def find_words(text_file):
    words = text_file.read().lower().split()
    words = [strip_non_characters(word) for word in words]
    return collections.Counter(words)


def save_material_word(material_obj, word, frequency):
    word_obj = Word.objects.get(word=word)
    try:
        MaterialWord.objects.get(word=word_obj, material=material_obj)
    except MaterialWord.DoesNotExist:
        MaterialWord.objects.create(word=word_obj, material=material_obj, frequency=frequency)


def save_material_words(material_obj, words):
    dictionary_words = Word.objects.values_list('word', flat=True)
    print len(words)
    for (word, count) in words.most_common():
        if word in dictionary_words:
            save_material_word(material_obj, word, count)
        elif strip_suffixes(word) in dictionary_words:
            save_material_word(material_obj, strip_suffixes(word), count)
        # else:
        #     if count > 1:
        #     print word, count


def not_found_words(material):
    material_words = material.materialword_set.all()
    dictionary_words = Word.objects.all()
    for word in dictionary_words:
        if word not in material_words:
            pass