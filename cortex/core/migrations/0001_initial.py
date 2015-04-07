# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cortex.core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('modType', models.CharField(choices=[('0', 'Forge'), ('1', 'Bukkit')], max_length=1, blank=True)),
                ('visibility', models.CharField(choices=[('0', 'Visible'), ('1', 'Hidden'), ('2', 'Private')], max_length=1)),
                ('logo', models.ImageField(upload_to=cortex.core.models.Mod.generate_imagefilename, blank=True)),
                ('website', models.URLField()),
                ('description', models.TextField()),
                ('license', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModVersion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=40, blank=True)),
                ('filename', models.CharField(max_length=120, blank=True)),
                ('file', models.FileField(upload_to=cortex.core.models.ModVersion.generate_filename)),
                ('mod', models.ForeignKey(to='core.Mod')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('isVerified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='modversion',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='mod',
            name='authors',
            field=models.ForeignKey(to='core.Person', blank=True),
        ),
        migrations.AddField(
            model_name='mod',
            name='latest',
            field=models.OneToOneField(to='core.ModVersion', related_name='latest_mod'),
        ),
        migrations.AddField(
            model_name='mod',
            name='recommended',
            field=models.OneToOneField(to='core.ModVersion', related_name='recommended_mod'),
        ),
        migrations.AddField(
            model_name='mod',
            name='tags',
            field=models.ManyToManyField(to='core.Tag', blank=True),
        ),
    ]
