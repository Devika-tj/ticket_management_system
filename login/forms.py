from django import forms
from django.contrib.auth.forms import AuthenticationForm


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