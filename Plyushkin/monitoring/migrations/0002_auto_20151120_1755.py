# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='resource',
            field=models.ForeignKey(to='monitoring.Resource', blank=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='schedule',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='exclude',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='include',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='path',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='source',
            field=models.ForeignKey(to='monitoring.Source', blank=True),
        ),
    ]
