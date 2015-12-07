# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20151120_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='resource',
            field=models.ForeignKey(blank=True, to='monitoring.Resource', null=True),
        ),
    ]
