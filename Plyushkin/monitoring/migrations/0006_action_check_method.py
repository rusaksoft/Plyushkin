# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_storage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='check_method',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
