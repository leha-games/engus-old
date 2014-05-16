# -*- coding: utf-8 -*-
import collections
import mimetypes
from django.core.exceptions import ValidationError
from engus.apps.dictionary.models import Word
from .models import MaterialWord


def find_words(text_file):
    # acceptable_file_types = ['text/plain', ]
    # if not mimetypes.guess_type(text_file) in acceptable_file_types:
    words = text_file.read().lower().split()
    return collections.Counter(words)
    # else:
    #     raise ValidationError('Not an acceptable file type')


def save_material_words(material, words):
    dictionary_words = Word.objects.values_list('word', flat=True)
    for (word, count) in words.most_common():
        if word in dictionary_words:
            word_obj = Word.objects.get(word=word)
            MaterialWord.objects.get_or_create(word=word_obj, material=material, frequency=count)


def not_found_words(material):
    material_words = material.materialword_set.all()
    dictionary_words = Word.objects.all()
    for word in dictionary_words:
        if word not in material_words:
                pass