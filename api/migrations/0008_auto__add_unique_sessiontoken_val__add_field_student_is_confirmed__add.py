# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'SessionToken', fields ['val']
        db.create_unique(u'api_sessiontoken', ['val'])

        # Adding field 'Student.is_confirmed'
        db.add_column(u'api_student', 'is_confirmed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Student.confirmation_code'
        db.add_column(u'api_student', 'confirmation_code',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'SessionToken', fields ['val']
        db.delete_unique(u'api_sessiontoken', ['val'])

        # Deleting field 'Student.is_confirmed'
        db.delete_column(u'api_student', 'is_confirmed')

        # Deleting field 'Student.confirmation_code'
        db.delete_column(u'api_student', 'confirmation_code')


    models = {
        u'api.company': {
            'Meta': {'ordering': "['id']", 'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        u'api.sessiontoken': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('val',),)", 'object_name': 'SessionToken'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'api.student': {
            'Meta': {'ordering': "['id']", 'object_name': 'Student'},
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '175'}),
            'first_hackathon': ('django.db.models.fields.BooleanField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'github_handle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linkedin_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'out_of_state': ('django.db.models.fields.BooleanField', [], {}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['api']