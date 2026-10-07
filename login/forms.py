from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from .models import User


class PENLoginForm(AuthenticationForm):

    username = forms.CharField(
        label="PEN Number",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your PEN number',
            'autofocus': True,
            'class': 'form-control',
        })
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control',
        })
    )


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'pen_number',
            'first_name',
            'last_name',
            'role',
            'is_active',
            'is_staff',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'pen_number',
            'first_name',
            'last_name',
            'email',
            'role',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )

        