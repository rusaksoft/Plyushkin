# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0004_auto_20151120_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
