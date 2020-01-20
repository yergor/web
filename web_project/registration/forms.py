from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import UserProfil


class registrationForm(UserCreationForm):   
    email = forms.EmailField(
        label='email',
        help_text='',
        max_length=50, 
        required=True,
    )

    nickname = forms.CharField(
        label='Отображаемое имя',
        help_text='',
        required=True,
    )

    password1 = forms.CharField(
        label='Пароль',
        help_text='',
        required=True,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Подтверждение пароля:',
        help_text='',
        required=True,
        widget=forms.PasswordInput,
    )
    password3 = forms.CharField(
        label='Подтверждение пароля:',
        help_text='',
        required=True,
        widget=forms.PasswordInput,
    )

class Meta:
    model = UserProfil
    fields = ('email',  'nickname',  'password1', 'password2',   'password3')