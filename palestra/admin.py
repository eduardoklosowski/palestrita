# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class TagInline(admin.TabularInline):
    model = models.Tag
    fields = ('nome', 'slug')
    extra = 1
    prepopulated_fields = {'slug': ('nome',)}


class VideoInline(admin.TabularInline):
    model = models.Video
    extra = 1


@admin.register(models.TipoTag)
class TipoTagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'cor', 'count_tags')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug', '=cor')
    fields = ('nome', 'slug', 'cor')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [TagInline]

    def count_tags(self, obj):
        return obj.tags.count()
    count_tags.short_description = '# Tags'


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome', 'slug', 'count_palestras')
    list_display_links = ('nome', 'slug')
    list_filter = ('tipo',)
    search_fields = ('nome', 'slug')
    fields = ('tipo', 'nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}

    def count_palestras(self, obj):
        return obj.palestras.count()
    count_palestras.short_description = '# Palestras'


@admin.register(models.Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'has_foto', 'has_info', 'count_palestras')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug')
    fields = ('nome', 'slug', 'foto', 'info')
    prepopulated_fields = {'slug': ('nome',)}

    def count_palestras(self, obj):
        return obj.palestras.count()
    count_palestras.short_description = '# Palestras'


@admin.register(models.Palestra)
class PalestraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'str_palestrantes', 'str_tags', 'count_videos')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug')
    fields = ('nome', 'slug', 'palestrantes', 'tags', 'info')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [VideoInline]

    def str_palestrantes(self, obj):
        return ', '.join((str(p) for p in obj.palestrantes.all()))
    str_palestrantes.short_description = 'Palestrantes'

    def str_tags(self, obj):
        return ', '.join((str(t) for t in obj.tags.all()))
    str_tags.short_description = 'Tags'

    def count_videos(self, obj):
        return obj.videos.count()
    count_videos.short_description = '# Vídeos'
