# -*- coding: utf-8 -*-

from django import forms

from . import models


def choices_tag():
    return [(i.nome, list(i.tags.values_list('slug', 'nome')))
            for i in models.TipoTag.objects.all()]


def choices_palestrante():
    palestrantes = list(models.Palestrante.objects.values_list('slug', 'nome'))
    palestrantes.insert(0, ('', '--------------------'))
    return palestrantes


class PalestraPesquisaForm(forms.Form):
    nome = forms.CharField(required=False)
    tag = forms.MultipleChoiceField(label='Nestas tags', required=False, choices=choices_tag)
    excludetag = forms.MultipleChoiceField(label='Não nestas tags', required=False, choices=choices_tag)
    palestrante = forms.ChoiceField(required=False, choices=choices_palestrante)
