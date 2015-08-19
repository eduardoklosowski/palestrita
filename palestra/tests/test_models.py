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
