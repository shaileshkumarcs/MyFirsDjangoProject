# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newswsletters', '0002_auto_20180210_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
