# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160119_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='created',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
        ),
    ]
