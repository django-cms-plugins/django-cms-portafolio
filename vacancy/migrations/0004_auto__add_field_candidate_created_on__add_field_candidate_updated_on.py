# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Candidate.created_on'
        db.add_column('vacancy_candidate', 'created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 1, 20), blank=True), keep_default=False)

        # Adding field 'Candidate.updated_on'
        db.add_column('vacancy_candidate', 'updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 1, 20), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Candidate.created_on'
        db.delete_column('vacancy_candidate', 'created_on')

        # Deleting field 'Candidate.updated_on'
        db.delete_column('vacancy_candidate', 'updated_on')


    models = {
        'vacancy.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'opening': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'candidates'", 'null': 'True', 'to': "orm['vacancy.EnableOpening']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'vacancy.enableopening': {
            'Meta': {'object_name': 'EnableOpening'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enable_openings'", 'to': "orm['vacancy.Opening']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'vacancy.opening': {
            'Meta': {'object_name': 'Opening'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'require': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'openings'", 'to': "orm['vacancy.Require']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'vacancy.require': {
            'Meta': {'object_name': 'Require'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['vacancy']
