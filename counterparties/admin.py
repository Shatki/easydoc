from django import forms
from django.contrib import admin
from .models import Counterpart, Bank


# Register your models here.
@admin.register(Counterpart)
class CounterpartAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'phone',
                    'email',
                    'site',
                    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'full_name',
            )}),
        (u'Контактная информация', {
            'fields': (
                'boss_first_name',
                'boss_second_name',
                'boss_last_name',
                'address',
                'post_address',
                'email',
                'site',
                'phone',
            )}),
        (u'Реквизиты', {
            'fields': (
                'account',
                'bik',
                'inn',
                'kpp',
                'ogrn',
                'okpo',
                'okato',
                'bank',
            )}),
        (u'Персонал', {
            'fields': (
                'employees',
            )}),
    )

    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'full_name',
                    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'full_name',
            )}),
        (u'Контактная информация', {
            'fields': (
                'address',
                'post_address',
                'email',
                'site',
                'phone',
            )}),
        (u'Реквизиты', {
            'fields': (
                'account',
                'bik',
                'inn',
                'kpp',
                'ogrn',
                'okpo',
                'okato',
            )}),
    )

    search_fields = ('name',)
    ordering = ('name',)
