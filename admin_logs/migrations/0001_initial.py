# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(help_text=b'Unique identifier of request. Should be unique accross all requests.', verbose_name=b'Hash', unique=True, max_length=100, editable=False)),
                ('start_date', models.DateTimeField(verbose_name=b'Request start time', editable=False, db_index=True)),
                ('duration', models.FloatField(verbose_name=b'Duration in milleseconds', editable=False)),
                ('max_level', models.SmallIntegerField(default=0, verbose_name=b'Max level', db_index=True, editable=False, choices=[(0, b'NOTSET'), (40, b'ERROR'), (20, b'INFO'), (10, b'DEBUG'), (50, b'CRITICAL'), (30, b'WARNING')])),
                ('url', models.CharField(verbose_name=b'Request url', max_length=255, editable=False, db_index=True)),
                ('status_code', models.SmallIntegerField(verbose_name=b'Status code', editable=False, db_index=True)),
                ('content_length', models.IntegerField(verbose_name=b'Content length', null=True, editable=False)),
                ('user_agent', models.CharField(max_length=255, null=True, editable=False)),
                ('ip', models.GenericIPAddressField(editable=False, db_index=True)),
                ('entries', picklefield.fields.PickledObjectField(default=[], editable=False)),
            ],
            options={
                'ordering': ['-start_date'],
            },
            bases=(models.Model,),
        ),
    ]
