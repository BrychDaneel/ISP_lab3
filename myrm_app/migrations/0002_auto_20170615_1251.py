# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='command',
            field=models.CharField(default='rm', max_length=30, choices=[(b'rm', b'Remove'), (b'rs', b'Restore'), (b'cl', b'Clean')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'waiting', max_length=30, choices=[(b'completed', b'Completed'), (b'canceled', b'Canceled'), (b'running', b'Running'), (b'completed', b'Completed')]),
        ),
    ]
