# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DefinitionExample'
        db.delete_table(u'dictionary_definitionexample')

        # Deleting model 'Sentence'
        db.delete_table(u'dictionary_sentence')

        # Adding field 'Definition.example'
        db.add_column(u'dictionary_definition', 'example',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Definition.example_russian_translation'
        db.add_column(u'dictionary_definition', 'example_russian_translation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Definition.example_illustration'
        db.add_column(u'dictionary_definition', 'example_illustration',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Definition.definition'
        db.alter_column(u'dictionary_definition', 'definition', self.gf('django.db.models.fields.TextField')(max_length=255))

        # Changing field 'Definition.russian_definition'
        db.alter_column(u'dictionary_definition', 'russian_definition', self.gf('django.db.models.fields.TextField')(max_length=255))

    def backwards(self, orm):
        # Adding model 'DefinitionExample'
        db.create_table(u'dictionary_definitionexample', (
            ('definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Definition'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('example', self.gf('django.db.models.fields.TextField')()),
            ('russian_translation', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dictionary', ['DefinitionExample'])

        # Adding model 'Sentence'
        db.create_table(u'dictionary_sentence', (
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sentence', self.gf('django.db.models.fields.TextField')()),
            ('translation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Sentence'])

        # Deleting field 'Definition.example'
        db.delete_column(u'dictionary_definition', 'example')

        # Deleting field 'Definition.example_russian_translation'
        db.delete_column(u'dictionary_definition', 'example_russian_translation')

        # Deleting field 'Definition.example_illustration'
        db.delete_column(u'dictionary_definition', 'example_illustration')


        # Changing field 'Definition.definition'
        db.alter_column(u'dictionary_definition', 'definition', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Definition.russian_definition'
        db.alter_column(u'dictionary_definition', 'russian_definition', self.gf('django.db.models.fields.TextField')())

    models = {
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'example': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'example_illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'example_russian_translation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'part_of_speach': ('django.db.models.fields.SmallIntegerField', [], {}),
            'russian_definition': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mueller_definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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