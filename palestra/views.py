# -*- coding: utf-8 -*-

from django.views import generic

from . import forms
from . import models


class PalestraPesquisaFormMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PalestraPesquisaFormMixin, self).get_context_data(**kwargs)
        context['palestra_pesquisa_form'] = forms.PalestraPesquisaForm(self.request.GET)
        return context


class IndexView(PalestraPesquisaFormMixin, generic.TemplateView):
    template_name = 'palestra/index.html'


class PalestraListView(PalestraPesquisaFormMixin, generic.ListView):
    model = models.Palestra

    def get_queryset(self):
        queryset = super(PalestraListView, self).get_queryset()

        filtroform = forms.PalestraPesquisaForm(self.request.GET)
        if filtroform.is_valid():
            if filtroform.cleaned_data.get('nome'):
                for palavra in filtroform.cleaned_data['nome'].split():
                    queryset = queryset.filter(nome__icontains=palavra)

            if filtroform.cleaned_data.get('tag'):
                tags = models.Tag.objects.filter(slug__in=filtroform.cleaned_data.get('tag'))
                for tag in tags:
                    queryset = queryset.filter(tags=tag)

            if filtroform.cleaned_data.get('excludetag'):
                tags = models.Tag.objects.filter(slug__in=filtroform.cleaned_data.get('excludetag'))
                for tag in tags:
                    queryset = queryset.exclude(tags=tag)

            if filtroform.cleaned_data.get('palestrante'):
                palestrante = models.Palestrante.objects.filter(slug=filtroform.cleaned_data.get('palestrante'))
                queryset = queryset.filter(palestrantes=palestrante)

        return queryset


class PalestraDetailView(PalestraPesquisaFormMixin, generic.DetailView):
    model = models.Palestra
