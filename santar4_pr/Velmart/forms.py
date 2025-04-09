from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CallBack


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ["name", "email", "subject", "message"]


class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Repeat', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


