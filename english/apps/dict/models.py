import uuid
import os
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.directory_string_var, filename)


class Word(models.Model):
    word = models.CharField(max_length=64, unique=True)


class Transcription(models.Model):
    word = models.ForeignKey(Word)
    transcription = models.CharField(max_length=64, blank=True)


class MullerDefinition(models.Model):
    word = models.ForeignKey(Word)
    definition = models.TextField(blank=True)


class WordForm(models.Model):
    PRESENT_PARTICIPLE = 1
    SIMPLE_PAST = 2
    PAST_PARTICIPLE = 3
    REGULAR_PLURAL = 4
    IRREGULAR_PLURAL = 5
    COMPARATIVE_ADJECTIVE = 6
    SUPERLATIVE_ADJECTIVE = 7
    DERIVATIVE = 8
    WORD_FORM_CHOICES = (
        ('Verb forms', (
                (PRESENT_PARTICIPLE, 'Present Participle'),
                (SIMPLE_PAST, 'Simple Past'),
                (PAST_PARTICIPLE, 'Past Participle'),
            )
        ),
        ('Plural forms', (
                (REGULAR_PLURAL, 'Regular Plural'),
                (IRREGULAR_PLURAL, 'Irregualar Plural'),
            )
        ),
        ('Adjective forms', (
                (COMPARATIVE_ADJECTIVE, 'Comparative adjective'),
                (SUPERLATIVE_ADJECTIVE, 'Superlative adjecitve'),
            )
        ),
        (DERIVATIVE, 'Derivative'),
    )
    word = models.ForeignKey(Word)
    form = models.SmallIntegerField(choices=WORD_FORM_CHOICES)
    headword = models.ForeignKey(Word, null=True, blank=True, related_name='headword_for')


class Definition(models.Model):
    NOUN = 1
    PRONOUN = 2
    ADJECTIVE = 3
    VERB = 4
    ADVERB = 5
    PREPOSITION = 6
    CONJUCTION = 7
    INTERJECTION = 8
    PART_OF_SPEACH_CHOICES = (
            (NOUN, 'Noun'),
            (PRONOUN, 'Pronoun'),
            (ADJECTIVE, 'Adjective'),
            (VERB, 'Verb'),
            (ADVERB, 'Adverb'),
            (PREPOSITION, 'Predosition'),
            (CONJUCTION, 'Conjuction'),
            (INTERJECTION, 'Interjection'),
    )

    def make_upload_path(instance, filename):
        return u"definition/%s/%s" % (instance.word.pk, filename)

    word = models.ForeignKey(Word)
    part_of_speach = models.SmallIntegerField(choices=PART_OF_SPEACH_CHOICES)
    language = models.SmallIntegerField(choices=LANGUAGE_CHOICES)
    definition = models.TextField()
    russuan_definition = models.TextField()
    weight = models.SmallIntegerField(default=0)
    illustration = models.ImageField(upload_to=make_upload_path, null=True, blank=True)


class DefinitionExample(models.Model):
    definition = models.ForeignKey(Definition)
    example = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    directory_string_var = 'books'


class BookChapter(models.Model):
    chapter = models.CharField(max_length=255)
    book = models.ForeignKey(Book)


class Sentence(models.Model):
    sentence = models.TextField()
    words = models.ManyToManyField(Word, null=True, blank=True)
    book = models.ForeignKey(Book, null=True, blank=True)
    page_of_book = models.PositiveIntegerField(blank=True, null=True)
