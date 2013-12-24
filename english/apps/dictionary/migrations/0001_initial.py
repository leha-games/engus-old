# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'dictionary_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'dictionary', ['Word'])

        # Adding model 'Transcription'
        db.create_table(u'dictionary_transcription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'])),
            ('transcription', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Transcription'])

        # Adding model 'MullerDefinition'
        db.create_table(u'dictionary_mullerdefinition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dictionary.Word'], unique=True)),
            ('definition', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['MullerDefinition'])

        # Adding model 'WordForm'
        db.create_table(u'dictionary_wordform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'])),
            ('form', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('headword', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='headword_for', null=True, to=orm['dictionary.Word'])),
        ))
        db.send_create_signal(u'dictionary', ['WordForm'])

        # Adding model 'Definition'
        db.create_table(u'dictionary_definition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'])),
            ('part_of_speach', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('definition', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('russian_definition', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('illustration', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Definition'])

        # Adding model 'DefinitionExample'
        db.create_table(u'dictionary_definitionexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Definition'])),
            ('example', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dictionary', ['DefinitionExample'])

        # Adding model 'Book'
        db.create_table(u'dictionary_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Book'])

        # Adding model 'BookChapter'
        db.create_table(u'dictionary_bookchapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chapter', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Book'])),
        ))
        db.send_create_signal(u'dictionary', ['BookChapter'])

        # Adding model 'Sentence'
        db.create_table(u'dictionary_sentence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sentence', self.gf('django.db.models.fields.TextField')()),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Book'], null=True, blank=True)),
            ('page_of_book', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Sentence'])

        # Adding M2M table for field words on 'Sentence'
        m2m_table_name = db.shorten_name(u'dictionary_sentence_words')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sentence', models.ForeignKey(orm[u'dictionary.sentence'], null=False)),
            ('word', models.ForeignKey(orm[u'dictionary.word'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sentence_id', 'word_id'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'dictionary_word')

        # Deleting model 'Transcription'
        db.delete_table(u'dictionary_transcription')

        # Deleting model 'MullerDefinition'
        db.delete_table(u'dictionary_mullerdefinition')

        # Deleting model 'WordForm'
        db.delete_table(u'dictionary_wordform')

        # Deleting model 'Definition'
        db.delete_table(u'dictionary_definition')

        # Deleting model 'DefinitionExample'
        db.delete_table(u'dictionary_definitionexample')

        # Deleting model 'Book'
        db.delete_table(u'dictionary_book')

        # Deleting model 'BookChapter'
        db.delete_table(u'dictionary_bookchapter')

        # Deleting model 'Sentence'
        db.delete_table(u'dictionary_sentence')

        # Removing M2M table for field words on 'Sentence'
        db.delete_table(db.shorten_name(u'dictionary_sentence_words'))


    models = {
        u'dictionary.book': {
            'Meta': {'object_name': 'Book'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dictionary.bookchapter': {
            'Meta': {'object_name': 'BookChapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Book']"}),
            'chapter': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'part_of_speach': ('django.db.models.fields.SmallIntegerField', [], {}),
            'russian_definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.definitionexample': {
            'Meta': {'object_name': 'DefinitionExample'},
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Definition']"}),
            'example': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dictionary.mullerdefinition': {
            'Meta': {'object_name': 'MullerDefinition'},
            'definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dictionary.Word']", 'unique': 'True'})
        },
        u'dictionary.sentence': {
            'Meta': {'object_name': 'Sentence'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Book']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_of_book': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dictionary.Word']", 'null': 'True', 'blank': 'True'})
        },
        u'dictionary.transcription': {
            'Meta': {'object_name': 'Transcription'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transcription': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'dictionary.wordform': {
            'Meta': {'object_name': 'WordForm'},
            'form': ('django.db.models.fields.SmallIntegerField', [], {}),
            'headword': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'headword_for'", 'null': 'True', 'to': u"orm['dictionary.Word']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        }
    }

    complete_apps = ['dictionary']