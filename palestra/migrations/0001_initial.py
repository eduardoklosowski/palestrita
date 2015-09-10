# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palestra',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('info', models.TextField(blank=True, verbose_name='informações')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('foto', models.URLField(blank=True)),
                ('info', models.TextField(blank=True, verbose_name='informações')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('nome', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='TipoTag',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('nome', models.CharField(unique=True, max_length=32)),
                ('cor', models.CharField(validators=[django.core.validators.RegexValidator('^#[0-9A-Fa-f]{6}$')], default='#000000', max_length=7)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('palestra', models.ForeignKey(related_name='videos', to='palestra.Palestra')),
            ],
            options={
                'ordering': ('palestra', 'url'),
                'verbose_name': 'vídeo',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='tipo',
            field=models.ForeignKey(related_name='tags', to='palestra.TipoTag'),
        ),
        migrations.AddField(
            model_name='palestra',
            name='palestrantes',
            field=models.ManyToManyField(blank=True, related_name='palestras', to='palestra.Palestrante'),
        ),
        migrations.AddField(
            model_name='palestra',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='palestras', to='palestra.Tag'),
        ),
    ]
