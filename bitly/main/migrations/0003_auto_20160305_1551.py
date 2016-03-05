# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160303_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlredirect',
            name='original_url',
            field=models.CharField(max_length=2000),
        ),
    ]
