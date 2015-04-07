# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cortex.core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mod',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('modType', models.CharField(blank=True, max_length=1, choices=[('0', 'Forge'), ('1', 'Bukkit')])),
                ('visibility', models.CharField(max_length=1, choices=[('0', 'Visible'), ('1', 'Hidden'), ('2', 'Private')])),
                ('logo', models.ImageField(blank=True, upload_to=cortex.core.models.mod.generate_imagefilename)),
                ('website', models.URLField()),
                ('description', models.TextField()),
                ('license', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='modVersion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('version', models.CharField(blank=True, max_length=40)),
                ('filename', models.CharField(blank=True, max_length=120)),
                ('file', models.FileField(upload_to=cortex.core.models.modVersion.generate_filename)),
                ('mod', models.ForeignKey(to='core.mod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('isVerified', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='String',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='modversion',
            name='tags',
            field=models.ManyToManyField(to='core.String'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mod',
            name='authors',
            field=models.ForeignKey(to='core.person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mod',
            name='latest',
            field=models.OneToOneField(to='core.modVersion', related_name='latest_mod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mod',
            name='recommended',
            field=models.OneToOneField(to='core.modVersion', related_name='recommended_mod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mod',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.String'),
            preserve_default=True,
        ),
    ]
