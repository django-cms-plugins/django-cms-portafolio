# -*- coding: utf-8 -*-
from south.db import db
from django.db import models
from cms.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Page.menu_login_required'
        db.add_column('cms_page', 'menu_login_required', orm['cms.page:menu_login_required'])
        
       
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Page.menu_login_required'
        db.delete_column('cms_page', 'menu_login_required')
           
    
    
    models = {
        'auth.group': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('models.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('models.CharField', [], {'max_length': '100'}),
            'content_type': ('models.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('models.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('models.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('models.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('models.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('models.CharField', [], {'max_length': '128'}),
            'user_permissions': ('models.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('models.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cms.cmsplugin': {
            'creation_date': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'language': ('models.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'page': ('models.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'parent': ('models.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('models.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'plugin_type': ('models.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('models.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('models.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('models.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('models.PositiveIntegerField', [], {'db_index': 'True'})
        },
        
        'cms.globalpagepermission': {
            'can_add': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_change': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_change_advanced_settings': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'can_change_permissions': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'can_delete': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_moderate': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_move_page': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_publish': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_recover_page': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'group': ('models.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'sites': ('models.ManyToManyField', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'user': ('models.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cms.page': {
            'changed_by': ('models.CharField', [], {'max_length': '70'}),
            'created_by': ('models.CharField', [], {'max_length': '70'}),
            'creation_date': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'login_required': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'menu_login_required': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderator_state': ('models.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('models.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('models.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publication_date': ('models.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('models.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'publisher_is_draft': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('models.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('models.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('models.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('models.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('models.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('models.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'template': ('models.CharField', [], {'max_length': '100'}),
            'tree_id': ('models.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.pagemoderator': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'moderate_children': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderate_descendants': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderate_page': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'page': ('models.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'user': ('models.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cms.pagemoderatorstate': {
            'action': ('models.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'message': ('models.TextField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'page': ('models.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'user': ('models.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'cms.pagepermission': {
            'can_add': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_change': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_change_advanced_settings': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'can_change_permissions': ('models.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'can_delete': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_moderate': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_move_page': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_publish': ('models.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'grant_on': ('models.IntegerField', [], {'default': '5'}),
            'group': ('models.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'page': ('models.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'user': ('models.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
       
        'cms.pageuser': {
            'created_by': ('models.ForeignKey', [], {'related_name': "'created_users'", 'to': "orm['auth.User']"}),
            'user_ptr': ('models.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'cms.pageusergroup': {
            'created_by': ('models.ForeignKey', [], {'related_name': "'created_usergroups'", 'to': "orm['auth.User']"}),
            'group_ptr': ('models.OneToOneField', [], {'to': "orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'})
        },
       
        'cms.title': {
            'Meta': {'unique_together': "(('publisher_is_draft', 'language', 'page'),)"},
            'application_urls': ('models.CharField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'creation_date': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'has_url_overwrite': ('models.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'language': ('models.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'menu_title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('models.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page': ('models.ForeignKey', [], {'related_name': "'title_set'", 'to': "orm['cms.Page']"}),
            'page_title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'path': ('models.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'publisher_is_draft': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('models.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Title']"}),
            'publisher_state': ('models.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'redirect': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'model': ('models.CharField', [], {'max_length': '100'}),
            'name': ('models.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['cms']
