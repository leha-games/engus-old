import uuid
import os
from django.db import models
from django.contrib.auth.models import User


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.directory_string_var, filename)


class Word(models.Model):
    word = models.CharField(max_length=32, primary_key=True)
    transcription = models.CharField(max_length=64, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    audio = models.FileField(upload_to='word', null=True, blank=True)

    class Meta:
        ordering = ['word', ]

    def __unicode__(self):
        return self.word


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
    headword = models.ForeignKey(Word, null=True, blank=True, related_name='headword_for_words')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


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
        (NOUN, 'noun'),
        (PRONOUN, 'pronoun'),
        (ADJECTIVE, 'adjective'),
        (VERB, 'verb'),
        (ADVERB, 'adverb'),
        (PREPOSITION, 'predosition'),
        (CONJUCTION, 'conjuction'),
        (INTERJECTION, 'interjection'),
    )

    APPROVING = 1
    DISAPPROVING = 2
    FIGURATIVE = 3
    FORMAL = 4
    HUMOROUS = 5
    INFORMAL = 6
    IRONIC = 7
    LITERARY = 8
    OFFENSIVE = 9
    SLANG = 10
    TECHNICAL = 11
    OLDFASHIONED = 12
    OLDUSE = 13
    SAYING = 14
    LABEL_CHOICES = (
        (APPROVING, 'approving'),
        (DISAPPROVING, 'disapproving'),
        (FIGURATIVE, 'figurative'),
        (FORMAL, 'formal'),
        (HUMOROUS, 'humorous'),
        (INFORMAL, 'informal'),
        (IRONIC, 'ironic'),
        (LITERARY, 'literary'),
        (OFFENSIVE, 'offensive'),
        (SLANG, 'slang'),
        (TECHNICAL, 'technical'),
        (OLDFASHIONED, 'old-fashioned'),
        (OLDUSE, 'old use'),
        (SAYING, 'saying'),
    )


    def make_upload_path(instance, filename):
        return u"definition/%s/%s" % (instance.word.pk, filename)

    word = models.ForeignKey(Word)
    part_of_speach = models.SmallIntegerField(choices=PART_OF_SPEACH_CHOICES)
    weight = models.SmallIntegerField(default=0)
    label = models.SmallIntegerField(choices=LABEL_CHOICES, null=True, blank=True)
    definition = models.CharField(max_length=255, blank=True)
    explanation = models.CharField(max_length=100, blank=True)
    russian_definition = models.CharField(max_length=255, blank=True)
    illustration = models.ImageField(upload_to=make_upload_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s. %s. %d. %s' % (self.word, self.get_part_of_speach_display(), self.weight, self.definition)


class Example(models.Model):
    definition = models.ForeignKey(Definition)
    label = models.SmallIntegerField(choices=Definition.LABEL_CHOICES, null=True, blank=True)
    text = models.CharField(max_length=255)
    text_equal = models.CharField(max_length=100, blank=True)
    russian_translation = models.CharField(max_length=255, blank=True)
    illustration = models.ImageField(upload_to="definition_examples/%Y_%m_%d", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text
