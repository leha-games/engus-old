# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Example.text_equal'
        db.add_column(u'dictionary_example', 'text_equal',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Example.text_equal'
        db.delete_column(u'dictionary_example', 'text_equal')


    models = {
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'part_of_speach': ('django.db.models.fields.SmallIntegerField', [], {}),
            'russian_definition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.example': {
            'Meta': {'object_name': 'Example'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'russian_translation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text_equal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'short_translation': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'transcription': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'})
        },
        u'dictionary.wordform': {
            'Meta': {'object_name': 'WordForm'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.SmallIntegerField', [], {}),
            'headword': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'headword_for_words'", 'null': 'True', 'to': u"orm['dictionary.Word']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        }
    }

    complete_apps = ['dictionary']