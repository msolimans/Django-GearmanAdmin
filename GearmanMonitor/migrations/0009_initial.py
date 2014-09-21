# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Server'
        db.create_table(u'GearmanMonitor_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('port_no', self.gf('django.db.models.fields.IntegerField')(default=4730)),
        ))
        db.send_create_signal(u'GearmanMonitor', ['Server'])

        # Adding model 'Setting'
        db.create_table(u'GearmanMonitor_setting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'GearmanMonitor', ['Setting'])

        # Adding model 'RefreshRate'
        db.create_table(u'GearmanMonitor_refreshrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('rate_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_selected', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'GearmanMonitor', ['RefreshRate'])


    def backwards(self, orm):
        # Deleting model 'Server'
        db.delete_table(u'GearmanMonitor_server')

        # Deleting model 'Setting'
        db.delete_table(u'GearmanMonitor_setting')

        # Deleting model 'RefreshRate'
        db.delete_table(u'GearmanMonitor_refreshrate')


    models = {
        u'GearmanMonitor.refreshrate': {
            'Meta': {'object_name': 'RefreshRate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_selected': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'rate_value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'GearmanMonitor.server': {
            'Meta': {'object_name': 'Server'},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'port_no': ('django.db.models.fields.IntegerField', [], {'default': '4730'}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'GearmanMonitor.setting': {
            'Meta': {'object_name': 'Setting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['GearmanMonitor']