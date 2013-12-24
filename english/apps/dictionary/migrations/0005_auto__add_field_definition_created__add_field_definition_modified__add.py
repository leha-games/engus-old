# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Definition.created'
        db.add_column(u'dictionary_definition', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Definition.modified'
        db.add_column(u'dictionary_definition', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DefinitionExample.created'
        db.add_column(u'dictionary_definitionexample', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DefinitionExample.modified'
        db.add_column(u'dictionary_definitionexample', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sentence.created'
        db.add_column(u'dictionary_sentence', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sentence.modified'
        db.add_column(u'dictionary_sentence', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Word.created'
        db.add_column(u'dictionary_word', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Word.modified'
        db.add_column(u'dictionary_word', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'WordForm.created'
        db.add_column(u'dictionary_wordform', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'WordForm.modified'
        db.add_column(u'dictionary_wordform', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 24, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Definition.created'
        db.delete_column(u'dictionary_definition', 'created')

        # Deleting field 'Definition.modified'
        db.delete_column(u'dictionary_definition', 'modified')

        # Deleting field 'DefinitionExample.created'
        db.delete_column(u'dictionary_definitionexample', 'created')

        # Deleting field 'DefinitionExample.modified'
        db.delete_column(u'dictionary_definitionexample', 'modified')

        # Deleting field 'Sentence.created'
        db.delete_column(u'dictionary_sentence', 'created')

        # Deleting field 'Sentence.modified'
        db.delete_column(u'dictionary_sentence', 'modified')

        # Deleting field 'Word.created'
        db.delete_column(u'dictionary_word', 'created')

        # Deleting field 'Word.modified'
        db.delete_column(u'dictionary_word', 'modified')

        # Deleting field 'WordForm.created'
        db.delete_column(u'dictionary_wordform', 'created')

        # Deleting field 'WordForm.modified'
        db.delete_column(u'dictionary_wordform', 'modified')


    models = {
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'part_of_speach': ('django.db.models.fields.SmallIntegerField', [], {}),
            'russian_definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.definitionexample': {
            'Meta': {'object_name': 'DefinitionExample'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Definition']"}),
            'example': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'russian_translation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dictionary.sentence': {
            'Meta': {'object_name': 'Sentence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'translation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mueller_definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_translation': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'transcription': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'dictionary.wordform': {
            'Meta': {'object_name': 'WordForm'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.SmallIntegerField', [], {}),
            'headword': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'headword_for'", 'null': 'True', 'to': u"orm['dictionary.Word']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        }
    }

    complete_apps = ['dictionary']