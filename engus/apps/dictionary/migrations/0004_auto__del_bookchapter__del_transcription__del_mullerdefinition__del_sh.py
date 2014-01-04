# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BookChapter'
        db.delete_table(u'dictionary_bookchapter')

        # Deleting model 'Transcription'
        db.delete_table(u'dictionary_transcription')

        # Deleting model 'MullerDefinition'
        db.delete_table(u'dictionary_mullerdefinition')

        # Deleting model 'ShortDefintion'
        db.delete_table(u'dictionary_shortdefintion')

        # Deleting model 'Book'
        db.delete_table(u'dictionary_book')

        # Adding field 'Word.transcription'
        db.add_column(u'dictionary_word', 'transcription',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'Word.weight'
        db.add_column(u'dictionary_word', 'weight',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Word.short_translation'
        db.add_column(u'dictionary_word', 'short_translation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'Word.mueller_definition'
        db.add_column(u'dictionary_word', 'mueller_definition',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Sentence.page_of_book'
        db.delete_column(u'dictionary_sentence', 'page_of_book')

        # Deleting field 'Sentence.book'
        db.delete_column(u'dictionary_sentence', 'book_id')

        # Adding field 'Sentence.word'
        db.add_column(u'dictionary_sentence', 'word',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dictionary.Word']),
                      keep_default=False)

        # Adding field 'Sentence.translation'
        db.add_column(u'dictionary_sentence', 'translation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Sentence.level'
        db.add_column(u'dictionary_sentence', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field words on 'Sentence'
        db.delete_table(db.shorten_name(u'dictionary_sentence_words'))


    def backwards(self, orm):
        # Adding model 'BookChapter'
        db.create_table(u'dictionary_bookchapter', (
            ('chapter', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Book'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dictionary', ['BookChapter'])

        # Adding model 'Transcription'
        db.create_table(u'dictionary_transcription', (
            ('transcription', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dictionary', ['Transcription'])

        # Adding model 'MullerDefinition'
        db.create_table(u'dictionary_mullerdefinition', (
            ('definition', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('word', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dictionary.Word'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dictionary', ['MullerDefinition'])

        # Adding model 'ShortDefintion'
        db.create_table(u'dictionary_shortdefintion', (
            ('definition', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('word', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dictionary.Word'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('russian_definition', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['ShortDefintion'])

        # Adding model 'Book'
        db.create_table(u'dictionary_book', (
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'dictionary', ['Book'])

        # Deleting field 'Word.transcription'
        db.delete_column(u'dictionary_word', 'transcription')

        # Deleting field 'Word.weight'
        db.delete_column(u'dictionary_word', 'weight')

        # Deleting field 'Word.short_translation'
        db.delete_column(u'dictionary_word', 'short_translation')

        # Deleting field 'Word.mueller_definition'
        db.delete_column(u'dictionary_word', 'mueller_definition')

        # Adding field 'Sentence.page_of_book'
        db.add_column(u'dictionary_sentence', 'page_of_book',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Sentence.book'
        db.add_column(u'dictionary_sentence', 'book',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Book'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Sentence.word'
        db.delete_column(u'dictionary_sentence', 'word_id')

        # Deleting field 'Sentence.translation'
        db.delete_column(u'dictionary_sentence', 'translation')

        # Deleting field 'Sentence.level'
        db.delete_column(u'dictionary_sentence', 'level')

        # Adding M2M table for field words on 'Sentence'
        m2m_table_name = db.shorten_name(u'dictionary_sentence_words')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sentence', models.ForeignKey(orm[u'dictionary.sentence'], null=False)),
            ('word', models.ForeignKey(orm[u'dictionary.word'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sentence_id', 'word_id'])


    models = {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'russian_translation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dictionary.sentence': {
            'Meta': {'object_name': 'Sentence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'translation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']"})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mueller_definition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_translation': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'transcription': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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