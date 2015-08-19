# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class TagInline(admin.TabularInline):
    model = models.Tag
    extra = 0
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(models.TipoTag)
class TipoTagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'cor')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug', '=cor')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [TagInline]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome', 'slug')
    list_display_links = ('nome', 'slug')
    list_filter = ('tipo',)
    search_fields = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(models.Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'has_foto', 'has_info')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(models.Palestra)
class PalestraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'url')
    list_display_links = ('nome', 'slug')
    search_fields = ('nome', 'slug', 'url')
    prepopulated_fields = {'slug': ('nome',)}
