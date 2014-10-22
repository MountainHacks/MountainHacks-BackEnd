# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.major'
        db.add_column(u'api_student', 'major',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Student.gender'
        db.add_column(u'api_student', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1),
                      keep_default=False)

        # Adding field 'Student.github_handle'
        db.add_column(u'api_student', 'github_handle',
                      self.gf('django.db.models.fields.CharField')(default='Male', max_length=50),
                      keep_default=False)

        # Adding field 'Student.linkedin_link'
        db.add_column(u'api_student', 'linkedin_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)


        # Changing field 'Student.shirt_size'
        db.alter_column(u'api_student', 'shirt_size', self.gf('django.db.models.fields.CharField')(max_length=3))

    def backwards(self, orm):
        # Deleting field 'Student.major'
        db.delete_column(u'api_student', 'major')

        # Deleting field 'Student.gender'
        db.delete_column(u'api_student', 'gender')

        # Deleting field 'Student.github_handle'
        db.delete_column(u'api_student', 'github_handle')

        # Deleting field 'Student.linkedin_link'
        db.delete_column(u'api_student', 'linkedin_link')


        # Changing field 'Student.shirt_size'
        db.alter_column(u'api_student', 'shirt_size', self.gf('django.db.models.fields.CharField')(max_length=25))

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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'github_handle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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