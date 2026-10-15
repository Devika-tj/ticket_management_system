from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'SupportHub',
            {
                'fields': (
                    'full_name',
                    'phone',
                    'role',
                    'email_verified'
                )
            }
        ),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'SupportHub',
            {
                'fields': (
                    'full_name',
                    'phone',
                    'role',
                    'email_verified'
                )
            }
        ),
    )


 
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = (
        'username',
        'full_name',
        'role',
        'email',
        'is_active'
    )