# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.test import TestCase

from .. import models


class ValidatorsTest(TestCase):
    def test_validate_cor(self):
        models.validate_cor('#000000')
        models.validate_cor('#ffffff')
        models.validate_cor('#C5C5C5')
        with self.assertRaises(ValidationError):
            models.validate_cor('000000')
        with self.assertRaises(ValidationError):
            models.validate_cor('#00000')
        with self.assertRaises(ValidationError):
            models.validate_cor('#0000000')
        with self.assertRaises(ValidationError):
            models.validate_cor('#aaaaag')


class TipoTagModelTest(TestCase):
    def test_nome(self):
        tipotag = models.TipoTag(nome='nome')
        self.assertEqual(tipotag.nome, 'nome')

    def test_slug(self):
        tipotag = models.TipoTag(slug='slug')
        self.assertEqual(tipotag.slug, 'slug')

    def test_cor_default(self):
        tipotag = models.TipoTag()
        self.assertEqual(tipotag.cor, '#000000')

    def test_nome_unique(self):
        tipotagdb = models.TipoTag(nome='nomeunique', slug='nomeunique1')
        tipotagdb.full_clean()
        tipotagdb.save()

        tipotag = models.TipoTag(nome='nomeunique', slug='nomeunique2')
        with self.assertRaises(ValidationError):
            tipotag.full_clean()
            tipotag.save()

    def test_slug_unique(self):
        tipotagdb = models.TipoTag(nome='slugunique1', slug='slugunique')
        tipotagdb.full_clean()
        tipotagdb.save()

        tipotag = models.TipoTag(nome='slugunique2', slug='slugunique')
        with self.assertRaises(ValidationError):
            tipotag.full_clean()
            tipotag.save()

    def test_string(self):
        tipotag = models.TipoTag(nome='nome')
        self.assertEqual(str(tipotag), 'nome')


class TagModelTest(TestCase):
    def test_tipo(self):
        tipotag = models.TipoTag(nome='tipotag', slug='tipotag')

        tag = models.Tag(tipo=tipotag)
        self.assertEqual(tag.tipo, tipotag)

    def test_nome(self):
        tag = models.Tag(nome='nome')
        self.assertEqual(tag.nome, 'nome')

    def test_slug(self):
        tag = models.Tag(slug='slug')
        self.assertEqual(tag.slug, 'slug')

    def test_nome_unique(self):
        tipotag = models.TipoTag(nome='tipotag', slug='tipotag')
        tipotag.save()

        tagdb = models.Tag(tipo=tipotag, nome='nomeunique', slug='nomeunique1')
        tagdb.full_clean()
        tagdb.save()

        tag = models.Tag(tipo=tipotag, nome='nomeunique', slug='nomeunique2')
        with self.assertRaises(ValidationError):
            tag.full_clean()
            tag.save()

    def test_slug_unique(self):
        tipotag = models.TipoTag(nome='tipotag', slug='tipotag')
        tipotag.save()

        tagdb = models.Tag(tipo=tipotag, nome='slugunique1', slug='slugunique')
        tagdb.full_clean()
        tagdb.save()

        tag = models.Tag(tipo=tipotag, nome='slugunique2', slug='slugunique')
        with self.assertRaises(ValidationError):
            tag.full_clean()
            tag.save()

    def test_string(self):
        tag = models.Tag(nome='nome')
        self.assertEqual(str(tag), 'nome')


class PalestranteTest(TestCase):
    def test_nome(self):
        palestrante = models.Palestrante(nome='nome')
        self.assertEqual(palestrante.nome, 'nome')

    def test_slug(self):
        palestrante = models.Palestrante(slug='slug')
        self.assertEqual(palestrante.slug, 'slug')

    def test_foto(self):
        palestrante = models.Palestrante(foto='http://localhost/foto.jpg')
        self.assertEqual(palestrante.foto, 'http://localhost/foto.jpg')

    def test_info(self):
        palestrante = models.Palestrante(info='info')
        self.assertEqual(palestrante.info, 'info')

    def test_slug_unique(self):
        palestrantedb = models.Palestrante(nome='slugunique', slug='slugunique')
        palestrantedb.full_clean()
        palestrantedb.save()

        palestrante = models.Palestrante(nome='slugunique', slug='slugunique')
        with self.assertRaises(ValidationError):
            palestrante.full_clean()
            palestrante.save()

    def test_string(self):
        palestrante = models.Palestrante(nome='nome')
        self.assertEqual(str(palestrante), 'nome')


class PalestraTest(TestCase):
    def test_nome(self):
        palestra = models.Palestra(nome='nome')
        self.assertEqual(palestra.nome, 'nome')

    def test_slug(self):
        palestra = models.Palestra(slug='slug')
        self.assertEqual(palestra.slug, 'slug')

    def test_palestrantes(self):
        palestra = models.Palestra()
        palestra.save()
        self.assertListEqual(list(palestra.palestrantes.all()), [])

        palestrante = models.Palestrante(nome='nome', slug='slug')
        palestrante.save()
        palestra.palestrantes.add(palestrante)
        self.assertListEqual(list(palestra.palestrantes.all()), [palestrante])

    def test_tags(self):
        palestra = models.Palestra()
        palestra.save()
        self.assertListEqual(list(palestra.tags.all()), [])

        tipotag = models.TipoTag(nome='nome', slug='slug')
        tipotag.save()
        tag = models.Tag(tipo=tipotag, nome='nome', slug='slug')
        tag.save()
        palestra.tags.add(tag)
        self.assertListEqual(list(palestra.tags.all()), [tag])

    def test_info(self):
        palestra = models.Palestra(info='info')
        self.assertEqual(palestra.info, 'info')

    def test_url(self):
        palestra = models.Palestra(url='url')
        self.assertEqual(palestra.url, 'url')

    def test_slug_unique(self):
        palestradb = models.Palestra(nome='slugunique', slug='slugunique', url='http://localhost/videodb.ogv')
        palestradb.full_clean()
        palestradb.save()

        palestra = models.Palestra(nome='slugunique', slug='slugunique', url='http://localhost/video.ogv')
        with self.assertRaises(ValidationError):
            palestra.full_clean()
            palestra.save()

    def test_url_unique(self):
        palestradb = models.Palestra(nome='slugunique', slug='sluguniquedb', url='http://localhost/video.ogv')
        palestradb.full_clean()
        palestradb.save()

        palestra = models.Palestra(nome='slugunique', slug='sluguniquedb', url='http://localhost/video.ogv')
        with self.assertRaises(ValidationError):
            palestra.full_clean()
            palestra.save()

    def test_string(self):
        palestra = models.Palestra(nome='nome')
        self.assertEqual(str(palestra), 'nome')
