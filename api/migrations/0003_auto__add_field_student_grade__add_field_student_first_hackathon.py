# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.grade'
        db.add_column(u'api_student', 'grade',
                      self.gf('django.db.models.fields.CharField')(default='Freshman', max_length=75),
                      keep_default=False)

        # Adding field 'Student.first_hackathon'
        db.add_column(u'api_student', 'first_hackathon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.grade'
        db.delete_column(u'api_student', 'grade')

        # Deleting field 'Student.first_hackathon'
        db.delete_column(u'api_student', 'first_hackathon')


    models = {
        u'api.company': {
            'Meta': {'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        u'api.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '175'}),
            'first_hackathon': ('django.db.models.fields.BooleanField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'github_handle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linkedin_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'out_of_state': ('django.db.models.fields.BooleanField', [], {}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['api']