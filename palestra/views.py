# -*- coding: utf-8 -*-

from django.views import generic

from . import forms


class PalestraPesquisaFormMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PalestraPesquisaFormMixin, self).get_context_data(**kwargs)
        context['palestra_pesquisa_form'] = forms.PalestraPesquisaForm(self.request.GET)
        return context


class IndexView(PalestraPesquisaFormMixin, generic.TemplateView):
    template_name = 'palestra/index.html'
