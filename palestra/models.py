# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


validate_cor = RegexValidator('^#[0-9A-Fa-f]{6}$')


@python_2_unicode_compatible
class TipoTag(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True)
    cor = models.CharField(max_length=32, default='#000000', validators=[validate_cor])

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


@python_2_unicode_compatible
class Tag(models.Model):
    tipo = models.ForeignKey(TipoTag, related_name='tags')
    nome = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
