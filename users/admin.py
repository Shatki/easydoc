from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms

from .models import User


class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'email',
            'first_name',
            'last_name',
            'tag_line',
            'phone')
        readonly_fields = (
            'date_joined',
            'date_updated',)


class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'is_admin',
            'user_permissions',)


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'username',
        'email',
        'phone',
        'first_name',
        'last_name',
        'last_login')

    list_filter = (
        'date_joined',
        'last_login',
    )
    readonly_fields = (
        'date_joined',
        'date_updated',
        'last_login',
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'password',
            )
        }),

        (u'Персональная информация', {
            'fields': (
                'first_name',
                'last_name',
                'photo',
                'tag_line',
            )
        }),

        (u'Права доступа', {
            'fields': (
                'is_admin',
                'groups',
                'user_permissions',
            )
        }),

        (u'Важные даты', {
            'fields': (
                'last_login',
                'date_joined',
                'date_updated',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password',
                'is_admin',
            )
        }),
    )

    search_fields = (
        'name',
        'email',)

    ordering = (
        'date_joined',)

    filter_horizontal = (
        'groups',
        'user_permissions',)

# Register your models here.
