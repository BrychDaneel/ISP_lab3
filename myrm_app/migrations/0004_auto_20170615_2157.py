# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrm_app', '0003_auto_20170615_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'waiting', max_length=30, choices=[(b'completed', b'Waitint'), (b'canceled', b'Canceled'), (b'running', b'Running'), (b'completed', b'Completed'), (b'error', b'Error')]),
        ),
    ]
