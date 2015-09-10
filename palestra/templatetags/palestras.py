# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse


URL_PESQUISA = reverse('palestra:palestra_list')

register = template.Library()


@register.simple_tag
def tag_label(tag):
    return '<a href="%s?tag=%s"><span class="label round" style="background-color:%s">%s</span></a>' % \
        (URL_PESQUISA, tag.slug, tag.cor, tag.nome)


@register.simple_tag
def tags_labels(tags):
    return ' '.join(tag_label(tag) for tag in tags)


@register.simple_tag
def palestrante_link(palestrante):
    return '<a href="%s?palestrante=%s">%s</a>' % (URL_PESQUISA, palestrante.slug, palestrante.nome)


@register.simple_tag
def palestrantes_links(palestrantes):
    return ', '.join(palestrante_link(palestrante) for palestrante in palestrantes)


@register.simple_tag
def videos_links(videos):
    return ', '.join('<a href="%s" target="_blank">Link%s</a>' % (video.url, i)
                     for i, video in enumerate(videos, start=1))


@register.simple_tag
def videos_players(videos):
    return ''.join('<video src="%s" controls></video>' % video for video in videos)
