# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ObjectLog'
        db.create_table(u'fortytwoapps_objectlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('objectname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fortytwoapps', ['ObjectLog'])


    def backwards(self, orm):
        # Deleting model 'ObjectLog'
        db.delete_table(u'fortytwoapps_objectlog')


    models = {
        u'fortytwoapps.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'othercontacts': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'fortytwoapps.objectlog': {
            'Meta': {'object_name': 'ObjectLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'appname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objectname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fortytwoapps.request': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Request'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['fortytwoapps']