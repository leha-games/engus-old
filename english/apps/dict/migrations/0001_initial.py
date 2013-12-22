# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'dict_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pronunciation', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('form', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('headword', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='word_forms', null=True, to=orm['dict.Word'])),
        ))
        db.send_create_signal(u'dict', ['Word'])

        # Adding model 'Definition'
        db.create_table(u'dict_definition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dict.Word'])),
            ('part_of_speach', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('language', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('definition', self.gf('django.db.models.fields.TextField')()),
            ('weight', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('illustration', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'dict', ['Definition'])

        # Adding model 'DefinitionExample'
        db.create_table(u'dict_definitionexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dict.Definition'])),
            ('example', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dict', ['DefinitionExample'])

        # Adding model 'Book'
        db.create_table(u'dict_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'dict', ['Book'])

        # Adding model 'BookChapter'
        db.create_table(u'dict_bookchapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chapter', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dict.Book'])),
        ))
        db.send_create_signal(u'dict', ['BookChapter'])

        # Adding model 'Sentence'
        db.create_table(u'dict_sentence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sentence', self.gf('django.db.models.fields.TextField')()),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dict.Book'], null=True, blank=True)),
            ('page_of_book', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dict', ['Sentence'])

        # Adding M2M table for field words on 'Sentence'
        m2m_table_name = db.shorten_name(u'dict_sentence_words')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sentence', models.ForeignKey(orm[u'dict.sentence'], null=False)),
            ('word', models.ForeignKey(orm[u'dict.word'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sentence_id', 'word_id'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'dict_word')

        # Deleting model 'Definition'
        db.delete_table(u'dict_definition')

        # Deleting model 'DefinitionExample'
        db.delete_table(u'dict_definitionexample')

        # Deleting model 'Book'
        db.delete_table(u'dict_book')

        # Deleting model 'BookChapter'
        db.delete_table(u'dict_bookchapter')

        # Deleting model 'Sentence'
        db.delete_table(u'dict_sentence')

        # Removing M2M table for field words on 'Sentence'
        db.delete_table(db.shorten_name(u'dict_sentence_words'))


    models = {
        u'dict.book': {
            'Meta': {'object_name': 'Book'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dict.bookchapter': {
            'Meta': {'object_name': 'BookChapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dict.Book']"}),
            'chapter': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dict.definition': {
            'Meta': {'object_name': 'Definition'},
            'definition': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('django.db.models.fields.SmallIntegerField', [], {}),
            'part_of_speach': ('django.db.models.fields.SmallIntegerField', [], {}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dict.Word']"})
        },
        u'dict.definitionexample': {
            'Meta': {'object_name': 'DefinitionExample'},
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dict.Definition']"}),
            'example': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dict.sentence': {
            'Meta': {'object_name': 'Sentence'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dict.Book']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_of_book': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dict.Word']", 'null': 'True', 'blank': 'True'})
        },
        u'dict.word': {
            'Meta': {'object_name': 'Word'},
            'form': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'headword': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'word_forms'", 'null': 'True', 'to': u"orm['dict.Word']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pronunciation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['dict']