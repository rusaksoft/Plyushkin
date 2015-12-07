# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('notes', models.TextField()),
                ('dest_path', models.TextField()),
                ('schedule', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.TextField()),
                ('include', models.TextField()),
                ('exclude', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('login', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_type', models.TextField()),
                ('login', models.TextField()),
                ('password', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='source',
            field=models.ForeignKey(to='monitoring.Source'),
        ),
        migrations.AddField(
            model_name='action',
            name='resource',
            field=models.ForeignKey(to='monitoring.Resource'),
        ),
        migrations.AddField(
            model_name='action',
            name='storage',
            field=models.ForeignKey(to='monitoring.Storage'),
        ),
    ]
