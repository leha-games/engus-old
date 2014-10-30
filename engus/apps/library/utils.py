# -*- coding: utf-8 -*-
import collections
import re
from engus.apps.dictionary.models import Word
from .models import MaterialWord


def strip_suffix(word):
    return re.sub('(es|s|ies|ing|ed|er|est|ly|d)$', '', word)


def strip_remove_the_e_rule(word):
    return re.sub('(ed|ing)$', 'e', word)


def strip_double_the_final_consonant_rule(word):
    return re.sub(r'(\w)\1ing$', '\g<1>', word)


def strip_change_the_ie_to_y_rule(word):
    return re.sub('ying$', 'ie', word)


def find_words(text_file):
    words = re.findall(r'[A-Za-z]{2,}', text_file.read().lower())
    return collections.Counter(words)


def save_material_word(material_obj, word, frequency):
    word_obj = Word.objects.get(word=word)
    try:
        MaterialWord.objects.get(word=word_obj, material=material_obj)
    except MaterialWord.DoesNotExist:
        MaterialWord.objects.create(word=word_obj, material=material_obj, frequency=frequency)


def save_material_words(material_obj, words):
    all_dictionary_words = Word.objects.values_list('word', flat=True)
    print len(words)
    for (word, count) in words.most_common():
        if word in all_dictionary_words:
            save_material_word(material_obj, word, count)
        elif strip_suffix(word) in all_dictionary_words:
            save_material_word(material_obj, strip_suffix(word), count)
        elif strip_remove_the_e_rule(word) in all_dictionary_words:
            save_material_word(material_obj, strip_remove_the_e_rule(word), count)
        elif strip_double_the_final_consonant_rule(word) in all_dictionary_words:
            save_material_word(material_obj, strip_double_the_final_consonant_rule(word), count)
        elif strip_change_the_ie_to_y_rule(word) in all_dictionary_words:
            save_material_word(material_obj, strip_change_the_ie_to_y_rule(word), count)
        # else:
            # if count > 1:
            # print word, count