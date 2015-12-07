# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_auto_20151120_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='status',
            field=models.TextField(blank=True),
        ),
    ]
