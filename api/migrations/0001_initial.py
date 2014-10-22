# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'api_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=175)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('out_of_state', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'api', ['Student'])

        # Adding model 'Company'
        db.create_table(u'api_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=150)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'api', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'api_student')

        # Deleting model 'Company'
        db.delete_table(u'api_company')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'out_of_state': ('django.db.models.fields.BooleanField', [], {}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['api']