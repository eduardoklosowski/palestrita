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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
                ('info', models.TextField(verbose_name='informações', blank=True)),
                ('url', models.URLField(verbose_name='URL', unique=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
                ('foto', models.URLField(blank=True)),
                ('info', models.TextField(verbose_name='informações', blank=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='TipoTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('cor', models.CharField(validators=[django.core.validators.RegexValidator('^#[0-9A-Fa-f]{6}$')], max_length=32, default='#000000')),
            ],
            options={
                'ordering': ('nome',),
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
            field=models.ManyToManyField(blank=True, to='palestra.Palestrante', related_name='palestras'),
        ),
        migrations.AddField(
            model_name='palestra',
            name='tags',
            field=models.ManyToManyField(blank=True, to='palestra.Tag', related_name='palestras'),
        ),
    ]
