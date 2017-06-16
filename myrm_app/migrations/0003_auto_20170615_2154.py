# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrm_app', '0002_auto_20170615_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='how_old',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='recursive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'waiting', max_length=30, choices=[(b'completed', b'Waitint'), (b'canceled', b'Canceled'), (b'running', b'Running'), (b'completed', b'Completed')]),
        ),
    ]
