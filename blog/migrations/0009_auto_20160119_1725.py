# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comments_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='created',
            field=models.DateTimeField(null=True, auto_now=True, auto_now_add=True),
        ),
    ]
