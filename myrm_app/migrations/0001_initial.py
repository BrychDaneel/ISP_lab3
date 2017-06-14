# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bukkit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('directory', models.CharField(unique=True, max_length=30, validators=[django.core.validators.RegexValidator(b'^\\w+$')])),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parametrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('force', models.BooleanField(default=False)),
                ('dryrun', models.BooleanField(default=False)),
                ('auto_replace', models.BooleanField(default=False)),
                ('allow_autoclean', models.BooleanField(default=True)),
                ('trash_max_size', models.BigIntegerField(default=1073741824)),
                ('trash_max_count', models.BigIntegerField(default=10000000)),
                ('autoclean_count', models.BigIntegerField(default=1000000)),
                ('autoclean_size', models.BigIntegerField(default=536870912)),
                ('autoclean_days', models.BigIntegerField(default=90)),
                ('autoclean_same_count', models.BigIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target', models.CharField(max_length=100)),
                ('created', models.TimeField(auto_now=True)),
                ('status', models.CharField(max_length=30, choices=[(b'rm', b'Remove'), (b'rs', b'Restore'), (b'cl', b'Clean')])),
                ('bukkit', models.ForeignKey(to='myrm_app.Bukkit', on_delete=django.db.models.deletion.PROTECT)),
                ('parametrs', models.OneToOneField(to='myrm_app.Parametrs')),
            ],
        ),
        migrations.AddField(
            model_name='bukkit',
            name='parametrs',
            field=models.OneToOneField(to='myrm_app.Parametrs'),
        ),
    ]
