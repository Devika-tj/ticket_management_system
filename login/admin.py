from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    # Forms used by Django admin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = (
        'pen_number',
        'first_name',
        'last_name',
        'role',
        'is_active',
    )

    list_filter = (
        'role',
        'is_active',
    )

    search_fields = (
        'pen_number',
        'first_name',
        'last_name',
    )

    ordering = ('pen_number',)

    fieldsets = (
        (None, {
            'fields': (
                'pen_number',
                'password',
            )
        }),

        ('Personal information', {
            'fields': (
                'first_name',
                'last_name',
                'email',
            )
        }),

        ('Permissions', {
            'fields': (
                'role',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),

            'fields': (
                'pen_number',
                'first_name',
                'last_name',
                'role',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            ),
        }),
    )