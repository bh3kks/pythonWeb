# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='created',
        ),
    ]
