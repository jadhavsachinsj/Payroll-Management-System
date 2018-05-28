from django import forms
# form django.contrib.admin.widgets
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter User Name here '}),
                               )

    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': ' Enter Password'}),
    )
