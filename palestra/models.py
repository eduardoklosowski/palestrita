# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.templatetags.static import static
from django.utils.encoding import python_2_unicode_compatible


validate_cor = RegexValidator('^#[0-9A-Fa-f]{6}$')


@python_2_unicode_compatible
class TipoTag(models.Model):
    slug = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=32, unique=True)
    cor = models.CharField(max_length=7, default='#000000', validators=[validate_cor])

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


@python_2_unicode_compatible
class Tag(models.Model):
    tipo = models.ForeignKey(TipoTag, related_name='tags')
    slug = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ('tipo', 'nome')

    def __str__(self):
        return self.nome

    @property
    def cor(self):
        return self.tipo.cor


@python_2_unicode_compatible
class Palestrante(models.Model):
    slug = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=256)
    foto = models.URLField(blank=True)
    info = models.TextField('informações', blank=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def has_foto(self):
        return bool(self.foto)
    has_foto.boolean = True
    has_foto.short_description = 'tem foto?'

    def has_info(self):
        return bool(self.info)
    has_info.boolean = True
    has_info.short_description = 'tem info?'

    @property
    def foto_link(self):
        if self.foto:
            return self.foto
        return static('palestra/avatar.png')


@python_2_unicode_compatible
class Palestra(models.Model):
    slug = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=256)
    palestrantes = models.ManyToManyField(Palestrante, related_name='palestras', blank=True)
    tags = models.ManyToManyField(Tag, related_name='palestras', blank=True)
    info = models.TextField('informações', blank=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


@python_2_unicode_compatible
class Video(models.Model):
    palestra = models.ForeignKey(Palestra, related_name='videos')
    url = models.URLField('URL', unique=True)

    class Meta:
        ordering = ('palestra', 'url')
        verbose_name = 'vídeo'

    def __str__(self):
        return self.url
