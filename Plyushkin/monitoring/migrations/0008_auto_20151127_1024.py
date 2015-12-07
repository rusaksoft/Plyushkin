# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_action_last_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='last_check',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
