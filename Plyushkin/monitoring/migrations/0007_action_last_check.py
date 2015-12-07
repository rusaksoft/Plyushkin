# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_action_check_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='last_check',
            field=models.DateField(null=True),
        ),
    ]
